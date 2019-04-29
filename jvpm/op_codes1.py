"""
All Methods for OP Codes go in this file
"""

import numpy


class op_codes:

    # emulates println for the different data types  ******going to be redone*****
    def invokeVirtual(stack_z, tag):
        if tag == "java/lang/SystemoutLjava/io/PrintStream;":
            print(stack_z.pop())
        elif tag == "java/io/PrintStreamprint(D)V":
            print(stack_z.pop())

        elif tag == "java/io/PrintStreamprint(Z)V":
            poppedValue = stack_z.pop()
            if poppedValue == 1:
                print("true")
            elif poppedValue == 0:
                print("false")
            else:
                print("this is not implemented.")
        elif tag == "java/io/PrintStreamprintln(Ljava/lang/String;)V":
            print(stack_z.pop())

    def op_code70(stack_z):  # remainder
        var1 = stack_z.pop() % stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code78(stack_z):  # shift left
        var1 = stack_z.pop() << stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code80(stack_z):  # bitwise OR
        var1 = stack_z.pop() | stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code7c(stack_z):  # shift right
        var1 = stack_z.pop() >> stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code7a(self, stack):  # arithmetic shift right
        # Assumes values put on the stack have already been converted to decimal integers
        value = stack.pop()
        shift_amount = stack.pop()

        result = value >> shift_amount
        stack.append(result)

    def op_code82(stack_z):  # bitwise XOR
        var1 = stack_z.pop() ^ stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code05(stack_z):  # loads 2 onto stack
        stack_z.append(2)
        return stack_z

    def op_code06(stack_z):  # loads 3 onto stack
        stack_z.append(3)
        return stack_z

    def op_code07(stack_z):  # loads 4 onto stack
        stack_z.append(4)
        return stack_z

    def op_code08(stack_z):  # loads 5 onto stack
        stack_z.append(5)
        return stack_z

    def op_code60(stack_z):  # add
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

    def op_code64(self, stack):  # subtract
        # Assumes values put on the stack have already been converted to decimal integers
        x = stack.pop()
        y = stack.pop()

        result = x - y
        stack.append(result)

    def op_code7e(stack_z):  # bitwise and
        var1 = stack_z.pop() & stack_z.pop()
        stack_z.append(var1)
        return stack_z

    def op_code6c(stack_z):  # integer division
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if var2 == 0:
            raise ArithmeticError("Dividing by zero")
        else:
            var1 /= var2

        stack_z.append(var1)
        return stack_z

    def op_code68(stack_z):  # multiplication
        MAX_JAVA_INT = 2147483647
        MIN_JAVA_INT = -2147483647
        var1 = stack_z.pop()
        var2 = stack_z.pop()

        if (var1 == var2) and var1 == MAX_JAVA_INT:
            var1 = 1

        elif (var1 == var2) and var1 == MIN_JAVA_INT:
            var1 = 0

        elif var1 == MAX_JAVA_INT:
            if (var2 % 2) != 0:
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

    def op_code74(stack_z):  # change to negative
        var1 = stack_z.pop() * -1
        stack_z.append(var1)
        return stack_z

    def op_code02(stack_z):  # loads -1 into the stack
        stack_z.append(-1)
        return stack_z

    def op_code03(stack_z):  # loads 0 into the stack
        stack_z.append(0)
        return stack_z

    def op_code04(stack_z):  # loads 1 into the stack
        stack_z.append(1)
        return stack_z

    # def op_code91(stack_z):
    #        var1 = stack_z.pop()
    #        if var1 >= 0:
    #                if (var1 % 256) == 0:
    #                        stack_z.append(bytes([0]))
    #                else:
    #                        if (var1 // 256) % 2 == 0:
    #                                var1 -= (256 * (var1//256))
    #                                stack_z.append(bytes[var1])
    #                        elif ((var1 // 256) % 2) > 1:
    #                                var1 -= (256 * (var1//256 + 1))
    #                                stack_z.append(bytearray([256-var1]))
    #                        else:
    #                                var1 -= (256 * (var1//256 + 1))
    #                                stack_z.append(bytes[var1])
    #        else:
    #                if (var1 % 256) == 0:
    #                        stack_z.append(bytes([0]))
    #                else:
    #                        var1 += (256 * (var1//256) * -1)
    #                        stack_z.append(bytes([var1]))
    #        return stack_z

    def op_code92(stack_z):
        var1 = stack_z.pop()
        if var1 >= 32 & var1 <= 127:
            stack_z.append(chr(var1))
        else:
            stack_z.append("?")
        return stack_z

    def op_code87(stack_z):
        stack_z.append(float(stack_z.pop()))
        return stack_z

    def op_code86(stack_z):
        return op_codes.op_code87(stack_z)

    def op_code85(stack_z):
        var1 = stack_z.pop()
        stack_z.append(int(var1))
        return stack_z

    def op_code1a(stack_z, varsarray):
        stack_z.append(varsarray[0])
        return stack_z

    def op_code1b(stack_z, varsarray):
        stack_z.append(varsarray[1])
        return stack_z

    def op_code1c(stack_z, varsarray):
        stack_z.append(varsarray[2])
        return stack_z

    def op_code1d(stack_z, varsarray):
        stack_z.append(varsarray[3])
        return stack_z

    def op_code15(stack_z, varsarray, index):
        if index > len(varsarray):
            raise IndexError
        else:
            stack_z.append(varsarray[index])
            return stack_z

    # def op_code36(stack_z, varsarray, index):
    #        if (index > len(varsarray)):
    #               raise IndexError
    #      else:
    #                stack_z.append(varsarray[index])
    #                return stack_z

    # def op_code3b(stack_z, varsarray):
    #                stack_z.append(varsarray[0])
    #                return stack_z

    # def op_code3c(stack_z, varsarray):
    #               stack_z.append(varsarray[1])
    #              return stack_z

    # def op_code3d(stack_z, varsarray):
    #               stack_z.append(varsarray[2])
    #                return stack_z

    # def op_code3e(stack_z, varsarray):
    #               stack_z.append(varsarray[3])
    #              return stack_z

    def op_code93(stack_z):  # int to short
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

    def op_code2e(array, index):
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
            stack_z.append(lmax + (var1 + var2 + lmax + 1))
        else:
            stack_z.append(var1 + var2)
        return stack_z

    def op_code6d(stack_z):
        var1 = stack_z.pop()
        var2 = stack_z.pop()
        if var1 == 0 or var2 == 0:
            raise ArithmeticError
        else:
            stack_z.append(var2 // var1)
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

    def op_code7b(stack_z):
        var1 = stack_z.pop()
        var2 = stack_z.pop()
        lmin = -9223372036854775808
        lmax = 9223372036854775807

        if (var1 < 0 and var1 > lmin) and (var2 == lmin or var2 == lmax):
            if var2 == lmax:
                stack_z.append(1 << (var1 * -1 - 2))
            else:
                stack_z.append((1 << (var1 * -1 - 1)) * -1)

        elif (var1 == lmin or var1 == lmax) and (var2 == lmin or var2 == lmax):
            if var2 == lmin:
                stack_z.append(-1)
            else:
                stack_z.append(lmax)

        elif (var1 == var2) and var1 == lmax:
            stack_z.append(0)

        elif (var1 == var2) and var2 == lmin:
            stack_z.append(lmin)

        else:
            stack_z.append(var2 >> var1)
        return stack_z
