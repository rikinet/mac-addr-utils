from unittest import TestCase

from . import normalize_v4_address, normalize_v6_address, is_global, is_link_local


class TestIpAddr(TestCase):
    def test_normalize_v4_address(self):
        self.assertEqual('1.2.3.4', normalize_v4_address('001.002.003.004'))

    def test_normalize_v6_address(self):
        self.assertEqual('2001:db8::1', normalize_v6_address('2001:0DB8:0000:0000:0000:0000:0000:0001'))

    def test_is_global(self):
        self.assertTrue(is_global('2001:e42:102:1815:160:16:227:20'))
        self.assertFalse(is_global('2001:db8::1'))
        self.assertFalse(is_global('::1'))

    def test_is_link_local(self):
        self.assertTrue(is_link_local('fe80::9ea3:baff:fe02:1832'))
        self.assertFalse(is_link_local('2001:db8::1'))
        self.assertFalse(is_link_local('::1'))
