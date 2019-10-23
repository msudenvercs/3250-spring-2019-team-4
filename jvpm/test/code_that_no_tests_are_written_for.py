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

# def test_opcode91(self): #convert int to byte
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

    #def op_code7b(stack_z):
    #    var1 = stack_z.pop()
    #    var2 = stack_z.pop()
    #    lmin = -9223372036854775808
    #    lmax = 9223372036854775807

    #    if (var1 < 0 and var1 > lmin) and (var2 == lmin or var2 == lmax):
    #        if var2 == lmax:
    #            stack_z.append(1 << (var1 * -1 - 2))
    #        else:
    #            stack_z.append((1 << (var1 * -1 - 1)) * -1)

    #    elif (var1 == lmin or var1 == lmax) and (var2 == lmin or var2 == lmax):
    #        if var2 == lmin:
    #            stack_z.append(-1)
    #        else:
    #            stack_z.append(lmax)

    #    elif (var1 == var2) and var1 == lmax:
    #        stack_z.append(0)

    #    elif (var1 == var2) and var2 == lmin:
    #        stack_z.append(lmin)

    #    else:
    #        stack_z.append(var2 >> var1)
    #    return stack_z

    #def format_constant_table(self):
    #    for constant in self.classfile_constant_table:
    #        self.constant_split = [
    #            constant[i : i + 2] for i in range(0, len(constant), 2)
    #        ]
    #        tag = self.constant_split[0]
    #        self.constant_helper(tag)
    #    return self.formatted_constant_table

    #def print_table_info(self):
    #    print("\n-----CONSTANT TABLE-----")
    #    counter = 1
    #    for i in self.formatted_constant_table:
    #        print(counter, i)
    #        counter = counter + 1
    #    print("opcodes:", self.opcodes)
    #    print("virtual:", self.virtual)
    #    if self.virtual != "":
    #        op_codes.invokeVirtual(self.stack_z, self.virtual)

    #def recursive(self, index):
    #    check = ""
    #    for call in self.formatted_constant_table[index]:
    #        if check == "UTF-8":
    #            self.virtual = self.virtual + call
    #        elif call == "UTF-8":
    #            check = call
    #        if isinstance(call, int):
    #            self.recursive(call - 1)
    #    return self.virtual

    #def constant_helper(self, tag):
    #    map = {
    #        "0C": self.tag_ref_helper,
    #        "0A": self.tag_ref_helper,
    #        "09": self.tag_ref_helper,
    #        "08": self.tag_ref_helper,
    #        "07": self.tag_ref_helper,
    #        "01": self.tag_utf8_helper,
    #        "03": self.int_helper,
    #        "04": self.float_helper
    #    }
    #    try:
    #        map[tag](tag)
    #    except KeyError:
    #        self.default(tag)

    #def tag_ref_helper(self, tag):
    #    self.constant_parts.append(ConstantPoolTag(tag).get_tag_type(tag))
    #    for i in range(1, len(self.constant_split), 2):
    #        ref = self.constant_split[i] + self.constant_split[i + 1]
    #        self.constant_parts.append(int(ref, 16))
    #    self.formatted_constant_table.append(self.constant_parts)
    #    self.constant_parts = []
