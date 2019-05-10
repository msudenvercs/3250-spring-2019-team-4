"""
All Methods for OP Codes go in this file
"""

import importlib
import os
import numpy

class op_codes:
    def invokevirtual(self, stack, call_path):  # invoke virtual
        """
                I thought it would be better to separate the file path from the method name
                so instead of call path being a single string containing the path+method e.g java/util/Scanner/nextInt
                it should be an array that contains 2 elements, the path, [java/util/Scanner], and the method [nextInt]
                This might not be the best way to do it but I couldn't think of a better one
                Stack implementation will be for another time
                """

        split_path = call_path[0].split("/")  # Separate path into components
        file_name = split_path[
            len(split_path) - 1
        ]  # File name will be the "anchor"
        file_path = ".".join(
            split_path[: len(split_path) - 1]
        )  # Path to the anchor
        method_name = call_path[
            1
        ]  # Not sure if this is correct for all invokevirtual, revision inevitable

        class_name = importlib.import_module(("." + file_name), file_path)
        # TODO Catch error where method that does not exist is called
        method_call = getattr(class_name, method_name)

        result = method_call()
        stack.append(result)
        return (
            result
        )  # Will remove when done with testing as the result should only be pushed onto the stack

    def irem(self):  # remainder
        var1 = stack_z.pop() % stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def ishl(self):  # int logical shift left
        var1 = stack_z.pop() << stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def ior(self):  # bitwise int OR
        var1 = stack_z.pop() | stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def iushr(self):  # int logical shift right
        var1 = stack_z.pop() >> stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def ishr(self):  # int arithmetic shift right
        # Assumes values put on the stack have already been converted to decimal integers
        value = stack.pop()
        shift_amount = stack.pop()

        result = value >> shift_amount
        stack.append(result)
        return stack

    def ixor(self):  # bitwise XOR
        var1 = stack_z.pop() ^ stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def iconst_2(self):  # loads int 2 onto stack
        stack_z.append(2)
        return stack_z

    def iconst_3(self):  # loads int 3 onto stack
        stack_z.append(3)
        return stack_z

    def iconst_4(self):  # loads int 4 onto stack
        stack_z.append(4)
        return stack_z

    def iconst_5(self):  # loads int 5 onto stack
        stack_z.append(5)
        return stack_z

    def iadd(self):  # int add
        MAX_JAVA_INT = 2147483647
        MIN_JAVA_INT = -2147483647
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if var1 >= MAX_JAVA_INT or var2 >= MAX_JAVA_INT:
            var1 += var2
            var1 += MIN_JAVA_INT
        elif var1 <= MIN_JAVA_INT or var2 <= MIN_JAVA_INT:
            var1 += var2
            var1 += MAX_JAVA_INT
        else:
            var1 += var2

        stack_z.append(var1)
        return stack_z

    def isub(self):  # int subtract
        # Assumes values put on the stack have already been converted to decimal integers
        x = stack.pop()
        y = stack.pop()

        result = x - y
        stack.append(result)
        return stack

    def iand(self):  # bitwise and for integers
        var1 = stack_z.pop() & stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def idiv(self):  # integer division
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if var2 == 0:
            raise ArithmeticError("Dividing by zero")
        else:
            var1 /= var2

        stack_z.append(var1)
        return stack_z

    def imul(stack_z):  # int multiplication
        MAX_JAVA_INT = 2147483647
        MIN_JAVA_INT = -2147483647
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if (var1 == var2) and var1 == MAX_JAVA_INT:
            var1 = 1

        elif (var1 == var2) and var1 == MIN_JAVA_INT:
            var1 = 0

        elif var1 == MAX_JAVA_INT:
            if (var2 % 2) == 0:
                var1 = var2 * -1
            else:
                var1 = MAX_JAVA_INT - (var2 - 1)

        elif var2 == MAX_JAVA_INT:
            if (var1 % 2) == 0:
                var1 = var1 * -1
            else:
                var1 = MAX_JAVA_INT - (var1 - 1)

        elif var1 == MIN_JAVA_INT:
            if (var2 % 2) == 0:
                var1 = 0
            else:
                var1 = MIN_JAVA_INT
        elif var2 == MIN_JAVA_INT:
            if (var1 % 2) == 0:
                var1 = 0
            else:
                var1 = MIN_JAVA_INT

        stack_z.append(var1)
        return stack_z

    def ineg( stack_z):  # change int to negative
        var1 = stack_z.pop() * -1
        stack_z.append(var1)
        return stack_z

    def iconst_m1( stack_z):  # loads int -1 into the stack
        stack_z.append(-1)
        return stack_z

    def iconst_0( stack_z):  # loads int 0 into the stack
        stack_z.append(0)
        return stack_z

    def iconst_1( stack_z):  # loads 1 into the stack
        stack_z.append(1)
        return stack_z

    def i2c( stack_z):  # converts int to character
        var1 = stack_z.pop()
        if var1 >= 32 & var1 <= 127:
            stack_z.append(chr(var1))
        else:
            stack_z.append("?")
        return stack_z

    def i2d( stack_z):  # converts int to double
        stack_z.append(float(stack_z.pop()))
        return stack_z

    def i2f( stack_z):  #converts int to float
        return op_codes.i2d(stack_z)

    def i2l( stack_z):  #converts int to long
        var1 = stack_z.pop()
        stack_z.append(int(var1))
        return stack_z

    def iload_0( stack_z, varsarray):  # load int value from local var 0
        stack_z.append(varsarray[0])
        return stack_z

    def iload_1( stack_z, varsarray):  # load int value from local var 1
        stack_z.append(varsarray[1])
        return stack_z

    def iload_2( stack_z, varsarray):  # load int value from local var 2
        stack_z.append(varsarray[2])
        return stack_z

    def iload_3( stack_z, varsarray):  # load int value from local var 3
        stack_z.append(varsarray[3])
        return stack_z

    def iload( stack_z, varsarray, index): # load int value from local var index
        if index > len(varsarray):
            raise IndexError
        else:
            stack_z.append(varsarray[index])
            return stack_z

    def i2s( stack_z):  # int to short
        MAX_JAVA_INT = 2147483647
        MIN_JAVA_INT = -2147483647
        var1 = stack_z.pop()
        while var1 >= 32768 or var1 <= -32769:
            if var1 == MAX_JAVA_INT:
                var1 = -1

            if var1 == MIN_JAVA_INT:
                var1 = 0

            if var1 == 32768:
                var1 = -32768

            if var1 == -32769:
                var1 = 32767

            if var1 > 32768:
                var1 = -32768 + (var1 + -32768)

            if var1 < -32768:
                var1 = 32768 + (var1 + 32768)

        stack_z.append(var1)
        return stack_z

    def iaload( array, index):  # load an int from an array
        if index < len(array):
            stack_z = []
            stack_z.append(array[index])
            return stack_z
        else:
            raise IndexError

    def long_builder(hex):
        return int(numpy.binary_repr(int(hex, 16), width=64), 2)

    def op_code16(hex):
        stack_z = []
        stack_z.append(op_codes.long_builder(hex))
        return stack_z

    def op_code1e(stack_z, local_vars):
        stack_z = op_codes.op_code16(local_vars[0])
        return stack_z

    def op_code1f(stack_z, local_vars):
        stack_z = op_codes.op_code16(local_vars[1])
        return stack_z

    def op_code20(stack_z, local_vars):
        stack_z = op_codes.op_code16(local_vars[2])
        return stack_z

    def op_code21(stack_z, local_vars):
        stack_z = op_codes.op_code16(local_vars[3])
        return stack_z

    def op_code61(stack_z):
        lmax = 9223372036854775807
        lmin = -9223372036854775808
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if var1 + var2 > lmax:
            stack_z.append(lmin + (var1 + var2 + lmin))
        elif var1 + var2 < lmin:
            stack_z.append(lmax + (var1 + var2 + lmax + 1) + 1)
        else:
            stack_z.append(var1 + var2)
        return stack_z

    def op_code6d(stack_z):
        var1 = stack_z.pop()
        var2 = stack_z.pop()
        if var1 == 0 or var2 == 0:
            raise ArithmeticError
        else:
            stack_z.append((var2 // var1)+1)
        return stack_z

    def op_code75(stack_z):
        lmin = -9223372036854775808
        var1 = stack_z.pop()

        if var1 == lmin:
            stack_z.append(lmin)
        else:
            stack_z.append(var1 * -1)
        return stack_z

    def op_code94(stack_z):
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if var1 == var2:
            stack_z.append(0)
        elif var1 > var2:
            stack_z.append(-1)
        else:
            stack_z.append(1)
        return stack_z

    def lxor(self, stack_z):  # bitwise XOR for longs
        local_vars1 = int(stack_z.pop(), 16)
        local_vars2 = int(stack_z.pop(), 16)
        local_vars = local_vars1 ^ local_vars2
        stack_z.append(local_vars)
        return stack_z


    def lor(self, stack_z):  # bitwise OR for longs
        local_vars1 = int(stack_z.pop(), 16)
        local_vars2 = int(stack_z.pop(), 16)
        local_vars = local_vars1 | local_vars2
        stack_z.append(local_vars)
        return stack_z
