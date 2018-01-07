from unittest import TestCase

from . import to_colon_separated, to_dot_separated


class TestMacAddr(TestCase):
    def test_to_colon_separated(self):
        self.assertEqual('0a:0b:0c:0d:0e:0f', to_colon_separated('0A0B0C0D0E0F'))
        self.assertEqual('01:02:03:04:05:06', to_colon_separated('1:2:3:4:5:6'))
        self.assertEqual('00:01:02:03:04:05', to_colon_separated('1.203.0405'))

    def test_to_dot_separated(self):
        self.assertEqual('0102.0304.0a0b', to_dot_separated('01:02:03:04:0A:0B'))
        self.assertEqual('0a0b.0c0d.0e0f', to_dot_separated('a:b:c:d:e:f'))
        self.assertEqual('0a0b.0c0d.0e0f', to_dot_separated('0a0b0c0d0e0f'))
