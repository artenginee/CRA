from unittest import TestCase, skip
from unittest.mock import Mock, patch
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):
    def setUp(self):
        super().setUp()

        self.hardware: FlashMemoryDevice = Mock()
        self.driver = DeviceDriver(self.hardware)

    # @patch.object(FlashMemoryDevice, 'read', side_effect=[0x10, 0x10, 0x10, 0x10, 0x10])
    def test_read_success(self):
        self.hardware.read.side_effect = [0x10, 0x10, 0x10, 0x10, 0x10]
        self.assertEqual(0x10, self.driver.read(0xFF))
        self.assertEqual(5, self.hardware.read.call_count)

    def test_read_fail(self):
        self.hardware.read.side_effect = [0x10, 0x10, 0x10, 0x11, 0x10]

        with self.assertRaises(Exception) as context:
            print(self.driver.read(0xFF))

        self.assertEqual('ReadFailException', str(context.exception))

    def test_write_success(self):
        # hardware call_once 필요
        self.hardware.read.return_value = 0xFF
        self.assertIsNone(self.driver.write(0xFF, 0x10))
        self.assertEqual(1, self.hardware.read.call_count)

    def test_write_fail(self):
        self.hardware.read.return_value = 0x10

        with self.assertRaises(Exception) as context:
            self.driver.write(0xFF, 0x10)

        self.assertEqual('WriteFailException', str(context.exception))

    def test_read_and_print(self):
        pass