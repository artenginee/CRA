from unittest import TestCase
from alu_result import ALU_result
from alu import ALU

class TestALU(TestCase):
    def setUp(self):
        self.alu = ALU()
        self.ret = ALU_result()

    def tearDown(self):
        super().tearDown()

    def test_test_ADD(self):
        self.alu.set_operand1(10)
        self.alu.set_operand2(20)
        self.alu.set_opcode("ADD")

        self.alu.enable_signal(self.ret)

        self.assertEqual(30, self.ret.get_result())
        self.assertEqual(0, self.ret.get_status())

        self.alu.set_operand1(-1)
        self.alu.set_operand2(20)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(1, self.ret.get_status())

        self.alu.set_operand1(10)
        self.alu.set_operand2(-1)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(2, self.ret.get_status())

    def test_test_SUB(self):
        self.alu.set_operand1(10)
        self.alu.set_operand2(20)
        self.alu.set_opcode("SUB")

        self.alu.enable_signal(self.ret)

        self.assertEqual(-10, self.ret.get_result())
        self.assertEqual(0, self.ret.get_status())

        self.alu.set_operand1(-1)
        self.alu.set_operand2(20)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(1, self.ret.get_status())

        self.alu.set_operand1(10)
        self.alu.set_operand2(-1)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(2, self.ret.get_status())

    def test_test_MUL(self):
        self.alu.set_operand1(10)
        self.alu.set_operand2(20)
        self.alu.set_opcode("MUL")

        self.alu.enable_signal(self.ret)

        self.assertEqual(200, self.ret.get_result())
        self.assertEqual(0, self.ret.get_status())

        self.alu.set_operand1(-1)
        self.alu.set_operand2(20)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(1, self.ret.get_status())

        self.alu.set_operand1(10)
        self.alu.set_operand2(-1)
        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(2, self.ret.get_status())

    def test_test_ETC(self):
        self.alu.set_operand1(10)
        self.alu.set_operand2(20)
        self.alu.set_opcode("DIV")

        self.alu.enable_signal(self.ret)

        self.assertEqual(65535, self.ret.get_result())
        self.assertEqual(3, self.ret.get_status())
