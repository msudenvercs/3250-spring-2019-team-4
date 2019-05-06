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
    
     #def test_opcode91(self): #convert int to byte
    #    test_stack = [1, 2, 2147483647, -214748367, 500, -500, 256, -256, 768, 770]
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([254]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([12]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytearray([256-12]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([-1]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([2]))
    #    test_stack = op_codes1.op_codes.op_code91(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([1]))