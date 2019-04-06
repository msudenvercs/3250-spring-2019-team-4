from jvpm.ConstantPoolTag import *
from jvpm.op_codes1 import *
import os


class JavaClassFile:
    classfile_constant_table = []
    classfile_constant_table_size = -1
    classfile_interface_table = []
    classfile_interface_table_size = -1
    classfile_interfaces = []
    classfile_field_table = []
    classfile_field_table_size = -1
    classfile_fields = []
    classfile_method_table = []
    classfile_method_table_size = -1
    classfile_methods = []
    classfile_attribute_table = []
    classfile_attribute_table_size = -1
    stack_z = []

    def get_magic_number(self):
        magic_num = ""

        # Magic number's length is 8 hexadecimal characters and are separated by 2 each [i.e CA FE BA BE]
        # So each "element" of the JavaClassFile type object with the data from the class file is 2 hexadecimal digits
        # This is not true for some of the other elements [e.g flags] but will work for getting the magic number
        # Especially since it is known that the magic number is always on the top of the file
        for i in range(4):
            # 02 for format's 2nd parameter means 2 digits, X means capital format, if I wanted it to be in 0xFF format
            # I would put in #04X, 0xff would be #04x
            magic_num += format(self.data[i], "02X")
        return magic_num

    def get_major(self):
        major_version = format(self.data[6], "02X") + format(self.data[7], "02X")

        return major_version

    def get_minor(self):
        minor_version = format(self.data[4], "02X") + format(self.data[5], "02X")

        return minor_version

    def get_pool_count_raw(self):
        pool_count_raw = format(self.data[8], "02X") + format(self.data[9], "02X")

        return pool_count_raw

    def get_pool_count(self):
        # Pool count should be made of 2 bytes so 04X is the format parameter
        pool_count = int(self.get_pool_count_raw(), 16) - 1
        pool_count = format(pool_count, "04X")

        return pool_count

    def get_pool_count_raw_int(self):
        return int(self.get_pool_count_raw(), 16)

    def get_pool_count_int(self):
        return int(self.get_pool_count(), 16)

    def get_constant_table(self):
        byte_location = 10  # First tag is at byte 10
        constant = ""
        constant_table = []
        size = 0
        # Loop will stop once all constant values have been collected
        for i in range(self.get_pool_count_int()):
            data_value = format(self.data[byte_location], "02X")
            # Tag represents a string, which means there is still a 2 byte size value that needs to be read
            if data_value == "01":
                constant += data_value
                # Get the 2 prefix bytes that describe the string size
                byte_location += 1
                data_value = format(self.data[byte_location], "02X")
                byte_location += 1
                data_value += format(self.data[byte_location], "02X")
                byte_location += 1
                constant += data_value
                size += 3
                # Get the offset for a string from the ConstantPoolTag Class
                num_bytes = int(data_value, 16)
                for k in range(byte_location, byte_location + int(num_bytes)):
                    constant += format(self.data[k], "02X")
                    size += 1

                constant_table.append(constant)
                constant = ""
                byte_location += int(num_bytes)
            # Tag represents something else, which means only that value needs to be read
            else:
                num_bytes = ConstantPoolTag(data_value).get_byte_length(data_value)
                constant += data_value
                byte_location += 1
                size += 1
                for j in range(byte_location, byte_location + int(num_bytes)):
                    constant += format(self.data[j], "02X")
                    size += 1

                constant_table.append(constant)
                constant = ""
                byte_location += int(num_bytes)

        self.classfile_constant_table_size = size
        self.classfile_constant_table = constant_table
        return constant_table

    # Following methods require the cpsize, which is returned with the constant table, might want a
    # separate constant later instead of calling the get_constant_table method for performance reasons

    # The access flags are "put together" [e.g ACC_PUBLIC and ACC_SUPER is 0x0021]
    def get_access_flag(self):
        cpsize = self.classfile_constant_table_size
        access_flag_byte1 = 10 + cpsize
        access_flag_byte2 = 11 + cpsize

        access_flag = (format(self.data[access_flag_byte1], "02X") +
                       format(self.data[access_flag_byte2], "02X"))
        return access_flag

    # Assumes that the size of the class index is 2 bytes from 4.4.1 of the java.class documentation
    def get_class_identifier(self):
        constant_table = self.classfile_constant_table
        cpsize = self.classfile_constant_table_size

        class_index_byte1 = 12 + cpsize
        class_index_byte2 = 13 + cpsize

        class_index = (format(self.data[class_index_byte1], "02X") +
                       format(self.data[class_index_byte2], "02X"))

        class_index = int(class_index, 16)
        class_identifier = constant_table[class_index]

        return class_identifier

    def get_superclass_identifier(self):
        constant_table = self.classfile_constant_table
        cpsize = self.classfile_constant_table_size

        superclass_index_byte1 = 14 + cpsize
        superclass_index_byte2 = 15 + cpsize
        # Index of the constant pool table
        superclass_index = (format(self.data[superclass_index_byte1], "02X") +
                            format(self.data[superclass_index_byte2], "02X"))
        superclass_index = int(superclass_index, 16)

        superclass_identifier = constant_table[superclass_index]

        return superclass_identifier

    def get_interface_count(self):
        cpsize = self.classfile_constant_table_size
        interface_count_index_byte1 = 16 + cpsize
        interface_count_index_byte2 = 17 + cpsize

        interface_count = (format(self.data[interface_count_index_byte1], "02X") +
                           format(self.data[interface_count_index_byte2], "02X"))

        return interface_count

    def get_interface_table(self):
        interface_count = int(self.get_interface_count(), 16)
        cpsize = self.classfile_constant_table_size
        interface_table = []
        size = 0

        byte_location = 18 + cpsize

        for i in range(interface_count):
            interface_index = ""
            interface_index += format(self.data[byte_location], "02X")
            byte_location += 1
            interface_index += format(self.data[byte_location], "02X")
            byte_location += 1
            interface_table.append(interface_index)
            size += 2

        self.classfile_interface_table = interface_table
        self.classfile_interface_table_size = size
        return interface_table

    def get_interfaces(self):
        interface_table = self.classfile_interface_table
        constant_table = self.classfile_constant_table
        interfaces = []

        for i in range(len(interface_table)):
            interfaces.append(constant_table[int(interface_table[i], 16)])

        return interfaces

    def get_field_count(self):
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size

        field_count_index_byte1 = 18 + cpsize + isize
        field_count_index_byte2 = 19 + cpsize + isize

        field_count = (format(self.data[field_count_index_byte1], "02X") +
                       format(self.data[field_count_index_byte2], "02X"))
        return field_count

    def get_field_table(self):
        field_count = int(self.get_field_count(), 16)
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size
        field_table = []
        size = 0

        byte_location = 20 + cpsize + isize

        if field_count != 0:
            for i in range(field_count):
                field_table_element = ""
                for j in range(8):  # field_info consists of 8 bytes (4x u2)
                    field_table_element += format(self.data[byte_location], "02X")
                    byte_location += 1
                    size += 1

                attribute_size = int(field_table_element[15:], 16)
                if attribute_size != 0:
                    for j in range(attribute_size):
                        attribute = ""
                        for k in range(6):
                            attribute += format(self.data[byte_location], "02X")
                            byte_location += 1
                            size += 1
                        field_table_element += attribute

                        attribute_info_length = int(attribute[4:12], 16)

                        attribute_info = ""
                        for k in range(attribute_info_length):
                            attribute_info += format(self.data[byte_location], "02X")
                            byte_location += 1
                            size += 1
                        field_table_element += attribute_info

                field_table.append(field_table_element)

        self.classfile_field_table = field_table
        self.classfile_field_table_size = size

        return field_table

    def get_fields(self):
        constant_table = self.classfile_constant_table
        field_table = self.classfile_field_table
        fields = {}
        for i in range(len(field_table)):
            field_name_index = int(field_table[i][4:8], 16)
            field_descriptor_index = int(field_table[i][8:12], 16)
            field_name = constant_table[field_name_index]
            field_descriptor = constant_table[field_descriptor_index]

            field_attribute_count = int(field_table[i][12:16], 16)
            attributes_raw = []
            attributes = {}

            for j in range(field_attribute_count):
                attribute = field_table[i][16:]
                attributes_raw.append(attribute)
            for j in range(len(attributes_raw)):
                attribute_name_index = int(attributes_raw[j][0:4], 16)
                attribute_name = constant_table[attribute_name_index]
                attribute_length = attributes_raw[j][4:12]
                attribute_info = attributes_raw[j][12:]

                attribute_key = "Attribute " + str(j + 1)

                attributes[attribute_key] = attribute_name
                attributes[attribute_key + " Length"] = attribute_length
                attributes[attribute_key + " Code"] = attribute_info

            field_key = "Field " + str(i + 1)

            fields[field_key] = field_name
            fields[field_key + " Descriptor"] = field_descriptor
            fields[field_key + " Attributes"] = attributes

        self.classfile_fields = fields

        return fields

    # Returns number of methods + the <init> system method, or n + 1
    def get_method_count(self):
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size
        fsize = self.classfile_field_table_size

        method_count_byte1 = 20 + cpsize + isize + fsize
        method_count_byte2 = 21 + cpsize + isize + fsize
        method_count = (format(self.data[method_count_byte1], "02X") +
                        format(self.data[method_count_byte2], "02X"))

        return method_count

    def get_method_table(self):
        method_count = int(self.get_method_count(), 16)
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size
        fsize = self.classfile_field_table_size
        method_table = []
        size = 0

        byte_location = 22 + cpsize + isize + fsize
        for i in range(method_count):
            method_table_element = ""
            for j in range(8):  # Method_info consists of 8 bytes (4x u2)
                method_table_element += format(self.data[byte_location], "02X")
                byte_location += 1
                size += 1
            attribute_count = int(method_table_element[12:16], 16)
            if attribute_count != 0:
                for j in range(attribute_count):
                    attribute = ""
                    for k in range(6):
                        attribute += format(self.data[byte_location], "02X")
                        byte_location += 1
                        size += 1
                    method_table_element += attribute

                    attribute_info_length = int(attribute[4:12], 16)  # attribute_length
                    # simply added all the bytes related to the attribute length
                    attribute_info = ""
                    for k in range(attribute_info_length):
                        attribute_info += format(self.data[byte_location], "02X")
                        byte_location += 1
                        size += 1
                    method_table_element += attribute_info

            method_table.append(method_table_element)

        self.classfile_method_table = method_table
        self.classfile_method_table_size = size
        return method_table

    def get_methods(self):
        constant_table = self.classfile_constant_table
        method_table = self.classfile_method_table
        methods = {}
        for i in range(len(method_table)):
            method_name_index = int(method_table[i][4:8], 16)
            method_descriptor_index = int(method_table[i][8:12], 16)
            method_name = constant_table[method_name_index]
            method_descriptor = constant_table[method_descriptor_index]

            method_attribute_count = int(method_table[i][12:16], 16)
            attributes_raw = []
            attributes = {}

            for j in range(method_attribute_count):
                attribute = method_table[i][16:]
                attributes_raw.append(attribute)
            for j in range(len(attributes_raw)):
                attribute_name_index = int(attributes_raw[j][0:4], 16)
                attribute_name = constant_table[attribute_name_index]
                attribute_length = attributes_raw[j][4:12]
                attribute_info = attributes_raw[j][12:]

                attribute_key = "Attribute " + str(j + 1)

                attributes[attribute_key] = attribute_name
                attributes[attribute_key + " Length"] = attribute_length
                attributes[attribute_key + " Code"] = attribute_info

            method_key = "Method " + str(i + 1)

            methods[method_key] = method_name
            methods[method_key + " Descriptor"] = method_descriptor
            methods[method_key + " Attributes"] = attributes

        self.classfile_methods = methods

        return methods

    def get_attribute_count(self):
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size
        fsize = self.classfile_field_table_size
        msize = self.classfile_method_table_size

        attribute_count_byte1 = 22 + cpsize + isize + fsize + msize
        attribute_count_byte2 = 23 + cpsize + isize + fsize + msize

        attribute_count = (format(self.data[attribute_count_byte1], "02X") +
                           format(self.data[attribute_count_byte2], "02X"))

        return attribute_count

    def get_attribute_table(self):
        attribute_count = int(self.get_attribute_count(), 16)
        cpsize = self.classfile_constant_table_size
        isize = self.classfile_interface_table_size
        fsize = self.classfile_field_table_size
        msize = self.classfile_method_table_size
        attribute_table = []
        size = 0

        byte_location = 24 + cpsize + isize + fsize + msize

        for i in range(attribute_count):
            attribute = ""
            for j in range(6):
                attribute += format(self.data[byte_location], "02X")
                byte_location += 1
                size += 1
            attribute_info_length = int(attribute[4:12], 16)
            for j in range(attribute_info_length):
                attribute += format(self.data[byte_location], "02X")
                byte_location += 1
                size += 1
            attribute_table.append(attribute)

        self.classfile_attribute_table = attribute_table
        self.classfile_attribute_table_size = size

        return attribute_table

    def get_constant_table_size(self):
        return self.classfile_constant_table_size

    def get_interface_table_size(self):
        return self.classfile_interface_table_size

    def get_field_table_size(self):
        return self.classfile_field_table_size

    def get_method_table_size(self):
        return self.classfile_method_table_size

    def get_attribute_table_size(self):
        return self.classfile_attribute_table_size

    #parses constant table to check for #3, #13, #18, #24, #25, and #26
    def decode_constant_table(constant_table):
        for i in constant_table:
            #strings will be replaced with hexadecimal
            if (i == "#3"):
                if (i == "#17"):
                    if (i == "#24"):
                        return "PrintStream"
                if (i == "#18"):
                    if (i == "#25"):
                        return "println"
                    elif (i == "#26"):
                        return "(I)V"
                return


    # For Testing

    def print_data(self):   # pragma: no cover
        print("Magic Number: " + self.get_magic_number())
        print("Major Version: " + self.get_major())
        print("Minor Version: " + self.get_minor())
        print("Pool Count: " + self.get_pool_count_raw())
        print("Pool Count - 1: " + self.get_pool_count())
        print("Constant Table: " + str(self.classfile_constant_table))
        print("Constant Table Size: " + str(self.classfile_constant_table_size))
        print("Access Flag: " + self.get_access_flag())
        print("Class Identifier: " + self.get_class_identifier())
        print("Super Class Identifier: " + self.get_superclass_identifier())
        print("Interface Count: " + self.get_interface_count())
        print("Interface Table: " + str(self.classfile_interface_table))
        print("Interface Table Size: " + str(self.classfile_interface_table_size))
        print("Interfaces: " + str(self.get_interfaces()))
        print("Field Count: " + self.get_field_count())
        print("Field Table: " + str(self.classfile_field_table))
        print("Field Table Size: " + str(self.classfile_field_table_size))
        print("Fields: " + str(self.classfile_fields))
        print("Method Count: " + self.get_method_count())
        print("Method Table: " + str(self.classfile_method_table))
        print("Method Table Size: " + str(self.classfile_method_table_size))
        print("Methods: " + str(self.classfile_methods))
        print("Attribute Count: " + self.get_attribute_count())
        print("Attribute Table: " + str(self.classfile_attribute_table))
        print("Attribute Table Size: " + str(self.classfile_attribute_table_size))

    # decoding constant pool and calling upcodes, TODO clean code
    formatted_constant_table = []
    constant_parts =[]
    constant_slpit = []
    upcodes = []

    def format_constant_table(self):
        counter = 1;
        for constant in self.classfile_constant_table:
            self.constant_split = [constant[i:i+2] for i in range(0, len(constant), 2)]
            tag = self.constant_split[0]
            self.constant_helper(tag)

        for i in self.formatted_constant_table:
            print(counter ,i)
            counter = counter +1

    def get_upcodes(self):
        index = 18
        for method in self.classfile_method_table:
            method_split = [method[i:i+2] for i in range(0, len(method), 2)]
            upcodes_len = method_split[index:index+4]
            hex = int("".join(map(str, upcodes_len)),16)
            self.upcodes.append(method_split[index+4:index+4+hex])
        return(self.upcodes)

    def get_virtual(self):
        index = 0
        for upcodes in self.get_upcodes():
            for upcode in upcodes:
                self.execute_upcodes(upcodes,upcode,index)
        if self.virtual != "":
            op_codes.invokeVirtual(self.stack_z,self.virtual)
        return self.virtual

    def execute_upcodes(self,upcodes, upcode,index):
        get_return = ""
        map = {
            "B2": self.upcode_b2,
            "B1": self.upcode_b1,
            "10": self.upcode_10
        }
        try:
            map[upcode](upcodes,upcode,index)
        except KeyError:
            self.default(upcode)

    def upcode_b2(self,upcodes,upcode,index):
        pool_index = upcodes.index(upcode)
        code_index = int("".join(map(str, upcodes[pool_index+1:pool_index+3])),16)
        self.recursive(code_index)

    def upcode_b1(self,upcodes,upcode,index):
        return None

    def upcode_10(self,upcodes,upcode,index):
        pool_index = upcodes.index(upcode)
        constant = int("".join(map(str, upcodes[pool_index+1:pool_index+2])),16)
        self.stack_z.append(constant)

    def default(self,upcode):
        return None

    #recursive method to interpret contant pool
    virtual = ""
    def recursive(self,index):
        check = ""
        for call in self.formatted_constant_table[index]:
            if check == "UTF-8":
                self.virtual = self.virtual + call
            elif call == "UTF-8":
                check = call
            if isinstance(call,int):
                self.recursive(call-1)

    def constant_helper(self, tag):
        map = {
            "0C": self.tag_ref_helper,
            "0A": self.tag_ref_helper,
            "09": self.tag_ref_helper,
            "08": self.tag_ref_helper,
            "07": self.tag_ref_helper,
            "01": self.tag_utf8_helper
        }
        try:
            map[tag](tag)
        except KeyError:
            self.default(tag)

    def tag_ref_helper(self,tag):
        self.constant_parts.append(ConstantPoolTag(tag).get_tag_type(tag))
        for i in range(1,len(self.constant_split),2):
            ref = self.constant_split[i]+self.constant_split[i+1]
            self.constant_parts.append(int(ref,16))
        self.formatted_constant_table.append(self.constant_parts)
        self.constant_parts = []

    def tag_utf8_helper(self,tag):
        self.constant_parts.append(ConstantPoolTag(tag).get_tag_type(tag))
        hex_list = []
        for i in self.constant_split[3:]:
            hex_list.append(chr(int(i, 16)))
        ref = "".join(map(str, hex_list))
        self.constant_parts.append(ref)
        self.formatted_constant_table.append(self.constant_parts)
        self.constant_parts = []





    # Print data from tables in a human readable format
    def display_data(self): # pragma: no cover TODO
        values = {}
        index = 1
        class_file_constant_table = self.classfile_constant_table
        class_file_interface_table = self.classfile_interface_table
        class_file_field_table = self.classfile_field_table
        print("-----CONSTANT TABLE-----\n")
        for i in range(len(self.classfile_constant_table)):
            tag = str(class_file_constant_table[i][0:2])
            data = class_file_constant_table[i][2:]

            if tag == "01":     # String
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                data = bytes.fromhex(data).decode('utf-8')
                values[index] = [tag_type, data]

            elif tag == "07":   # Class Ref
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                data = '#' + str(int(data, 16))
                values[index] = [tag_type, data]

            elif tag == "08":   # String Ref
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                data = '#' + str(int(data, 16))
                values[index] = [tag_type, data]

            elif tag == "09":   # Field Ref
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                data_index_01 = data[2:4]
                data_index_02 = data[4:]
                data = ('#' + str(int(data_index_01, 16)) + ', ' + '#' + str(int(data_index_02, 16)))
                values[index] = [tag_type, data]

            elif tag == "0A":   # Method Ref
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                data_index_01 = data[2:4]
                data_index_02 = data[4:]
                data = ('#' + str(int(data_index_01, 16)) + ', ' + '#' + str(int(data_index_02, 16)))
                values[index] = [tag_type, data]

            else:
                tag_type = ConstantPoolTag(tag).get_tag_type(tag)
                values[index] = [tag_type, data]

            index += 1
        for i in range(1, len(class_file_constant_table)):
            print(str(i) + ": " + str(values[i]))

        print("\n-----INTERFACE TABLE-----")

    # Python "Constructor"
    def __init__(self, file_name):
        # TODO: Make it so that the .class file can be specified by name, this could help in testing opcode reading

        # "with" operator deals with closing the input stream and also handles some exceptions
        # Second parameter simply means "read binary"
        class_file_path = ""
        class_file_name = file_name
        # class_file_directory = os.path.abspath(os.path.join(class_file_path, class_file_name))

        with open(class_file_name, 'rb') as class_file:
            # Literally sets the object of this class to whatever is on the other side of the equals sign
            # For example with object a of class x and self.data = 0 in constructor, print(a.data) would print 0
            self.data = class_file.read()

        self.get_constant_table()
        self.get_interface_table()
        self.get_interfaces()
        self.get_field_table()
        self.get_fields()
        self.get_method_table()
        self.get_methods()
        self.get_attribute_table()


# -----END OF METHOD DEFINITIONS-----
a = JavaClassFile("test.class")
a.print_data()
#a.format_constant_table()
#a.get_virtual()
a.display_data()


'''
    def op_code_caller(self, input):
        op_code_dict = {
            "0x60":op_codes1.op_codes.op_code60
            "0x7e":op_codes1.op_codes.op_code7e
            "0x02":op_codes1.op_codes.op_code02
            "0x03":op_codes1.op_codes.op_code03
            "0x04":op_codes1.op_codes.op_code04
            "0x05"op_codes1.op_codes.:op_code05
            "0x06":op_codes1.op_codes.op_code06
            "0x07":op_codes1.op_codes.op_code07
            "0x08":op_codes1.op_codes.op_code08
            "0x6C":op_codes1.op_codes.op_code6c
            "0x68":op_codes1.op_codes.op_code68
            "0x70":op_codes1.op_codes.op_code70
            "0x74":op_codes1.op_codes.op_code74
            "0x78":op_codes1.op_codes.op_code78
            "0x7A":op_codes1.op_codes.op_code7a
            "0x7C":op_codes1.op_codes.op_code7c
            "0x80":op_codes1.op_codes.op_code80
            "0x64":op_codes1.op_codes.op_code64
            "0x82":op_codes1.op_codes.op_code82
        }

        send(op_code_dict[input](stack_z))

'''
