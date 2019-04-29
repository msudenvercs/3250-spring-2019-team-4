from enum import Enum


class ConstantPoolTag(Enum):
    tag_01 = "01"
    tag_03 = "03"
    tag_04 = "04"
    tag_05 = "05"
    tag_06 = "06"
    tag_07 = "07"
    tag_08 = "08"
    tag_09 = "09"
    tag_10 = "0A"
    tag_11 = "0B"
    tag_12 = "0C"
    tag_15 = "0F"
    tag_16 = "10"
    tag_18 = "12"

    # Returns number of bytes for specific constant based on
    def get_byte_length(self, tag):
        return {
            "01": 2,  # This represents how many bytes the UTF-8 string size variable is [e.g 00 05]
            "03": 4,  # Integer
            "04": 4,  # Float
            "05": 8,  # Long
            "06": 8,  # Double, 64-bit
            "07": 2,  # Class Reference
            "08": 2,  # String Reference
            "09": 4,  # Field Reference
            "0A": 4,  # Method Reference
            "0B": 4,  # Interface Method Reference
            "0C": 4,  # Name and Type Descriptor
            "0F": 3,  # Method Handle
            "10": 2,  # Method Type
            "12": 4,  # InvokeDynamic
        }.get(tag, None)

    def get_tag_type(self, tag):
        return {
            "01": "UTF-8",  # This represents how many bytes the UTF-8 string size variable is [e.g 00 05]
            "03": "Integer",  # Integer
            "04": "Float",  # Float
            "05": "Long",  # Long
            "06": "Double",  # Double, 64-bit
            "07": "Class Reference",  # Class Reference
            "08": "String Reference",  # String Reference
            "09": "Field Reference",  # Field Reference
            "0A": "Method Reference",  # Method Reference
            "0B": "Interface Method",  # Interface Method Reference
            "0C": "Name and Type Desc.",  # Name and Type Descriptor
            "0F": "Method Handle",  # Method Handle
            "10": "Method Type",  # Method Type
            "12": "Dynamic",  # InvokeDynamic
        }.get(tag, None)
