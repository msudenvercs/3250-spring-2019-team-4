
import unittest
import io
import sys
from jvpm import ClassFile

class testClass(unittest.TestCase):
    unittest_file = ClassFile.JavaClassFile("test.class")

    def test_get_magic_number(self):
        self.assertEqual(ClassFile.JavaClassFile.get_magic_number(self.unittest_file), 'CAFEBABE')

    def test_get_major(self):
        self.assertEqual(ClassFile.JavaClassFile.get_minor(self.unittest_file), '0000')

    def test_get_minor(self):
        self.assertEqual(ClassFile.JavaClassFile.get_major(self.unittest_file), '0037')

    def test_get_pool_count_raw(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_raw(self.unittest_file), '0026')

    def test_get_pool_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count(self.unittest_file), '0025')

    def test_get_pool_count_raw_int(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_raw_int(self.unittest_file), int("0026", 16))

    def test_get_pool_count_int(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_int(self.unittest_file), int("0025", 16))

    def test_get_constant_table(self):
        expected_table = ['0A00090015',
                          '080016',
                          '0900080017',
                          '0900180019',
                          '07001A',
                          '08001B',
                          '0A001C001D',
                          '07001E',
                          '07001F',
                          '01000C6669656C645F737472696E67',
                          '0100124C6A6176612F6C616E672F537472696E673B',
                          '0100063C696E69743E',
                          '010003282956',
                          '010004436F6465',
                          '01000F4C696E654E756D6265725461626C65',
                          '0100046D61696E',
                          '010016285B4C6A6176612F6C616E672F537472696E673B2956',
                          '01000A68656C6C6F576F726C64',
                          '01000A536F7572636546696C65',
                          '010009746573742E6A617661',
                          '0C000C000D',
                          '0100035A5A5A',
                          '0C000A000B',
                          '070020',
                          '0C00210022',
                          '01000E746573745F696E74657266616365',
                          '01000548656C6C6F',
                          '070023',
                          '0C00240025',
                          '01000474657374',
                          '0100106A6176612F6C616E672F4F626A656374',
                          '0100106A6176612F6C616E672F53797374656D',
                          '0100036F7574',
                          '0100154C6A6176612F696F2F5072696E7453747265616D3B',
                          '0100136A6176612F696F2F5072696E7453747265616D',
                          '0100077072696E746C6E',
                          '010015284C6A6176612F6C616E672F537472696E673B2956']

        self.assertEqual(ClassFile.JavaClassFile.get_constant_table(self.unittest_file), expected_table)

    def test_get_constant_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_constant_table_size(self.unittest_file), 369)

    def test_get_access_flag(self):
        self.assertEqual(ClassFile.JavaClassFile.get_access_flag(self.unittest_file), "0021")

    def test_get_class_identifier(self):
        self.assertEqual(ClassFile.JavaClassFile.get_class_identifier(self.unittest_file), "07001F")

    def test_get_superclass_identifier(self):
        self.assertEqual(ClassFile.JavaClassFile.get_superclass_identifier(self.unittest_file),
                         "01000C6669656C645F737472696E67")

    def test_get_interface_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_interface_count(self.unittest_file), "0001")

    def test_get_interface_table(self):
        expected_table = ['0005']

        self.assertEqual(ClassFile.JavaClassFile.get_interface_table(self.unittest_file), expected_table)

    def test_get_interface_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_interface_table_size(self.unittest_file), 2)

    def test_get_interfaces(self):
        expected_table = ['08001B']

        self.assertEqual(ClassFile.JavaClassFile.get_interfaces(self.unittest_file), expected_table)

    def test_get_field_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_field_count(self.unittest_file), "0001")

    def test_get_field_table(self):
        expected_table = ['0000000A000B0000']
        self.assertEqual(ClassFile.JavaClassFile.get_field_table(self.unittest_file), expected_table)

    def test_get_field_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_field_table_size(self.unittest_file), 8)

    def test_get_fields(self):
        expected_table = {'Field 1': '0100124C6A6176612F6C616E672F537472696E673B',
                          'Field 1 Descriptor': '0100063C696E69743E',
                          'Field 1 Attributes':
                              {
                              }
                          }
        self.assertEqual(ClassFile.JavaClassFile.get_fields(self.unittest_file), expected_table)

    def test_get_method_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_method_count(self.unittest_file), "0003")

    def test_get_method_table(self):
        expected_table = ['0001000C000D0001000E00000027000200010000000B2AB700012A1202B50003B100000001000F0000000A00020000000100040002',
                          '0009001000110001000E000000260001000200000006043C840101B100000001000F0000000E0003000000040002000500050007',
                          '00010012000D0001000E000000250002000100000009B200041206B60007B100000001000F0000000A00020000000B0008000C']

        self.assertEqual(ClassFile.JavaClassFile.get_method_table(self.unittest_file), expected_table)

    def test_get_method_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_method_table_size(self.unittest_file), 156)

    def test_get_methods(self):
        expected_table = {'Method 1': '010003282956',
                          'Method 1 Descriptor': '010004436F6465',
                          'Method 1 Attributes':
                              {'Attribute 1': '01000F4C696E654E756D6265725461626C65',
                               'Attribute 1 Length': '00000027',
                               'Attribute 1 Code': '000200010000000B2AB700012A1202B50003B100000001000F0000000A00020000000100040002'
                               },
                          'Method 2': '010016285B4C6A6176612F6C616E672F537472696E673B2956',
                          'Method 2 Descriptor': '01000A68656C6C6F576F726C64',
                          'Method 2 Attributes':
                              {'Attribute 1': '01000F4C696E654E756D6265725461626C65',
                               'Attribute 1 Length': '00000026',
                               'Attribute 1 Code': '0001000200000006043C840101B100000001000F0000000E0003000000040002000500050007'
                               },
                          'Method 3': '01000A536F7572636546696C65',
                          'Method 3 Descriptor': '010004436F6465',
                          'Method 3 Attributes':
                              {'Attribute 1': '01000F4C696E654E756D6265725461626C65',
                               'Attribute 1 Length': '00000025',
                               'Attribute 1 Code': '0002000100000009B200041206B60007B100000001000F0000000A00020000000B0008000C'
                               }
                          }

        self.assertEqual(ClassFile.JavaClassFile.get_methods(self.unittest_file), expected_table)

    def test_get_attribute_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_attribute_count(self.unittest_file), "0001")

    def test_get_attribute_table(self):
        expected_table = ['0013000000020014']

        self.assertEqual(ClassFile.JavaClassFile.get_attribute_table(self.unittest_file), expected_table)

    def test_get_attribute_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_attribute_table_size(self.unittest_file), 8)

    def test_print_string(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unittest_file.print_string()
        self.assertEqual((capturedOutput), "This is COOL!")
