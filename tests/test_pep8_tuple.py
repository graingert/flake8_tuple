# -*- coding: utf-8 -*-
import unittest

from ddt import ddt, data, unpack

from flake8_tuple import check_code_for_wrong_tuple


@ddt
class Testflake8Tuple(unittest.TestCase):
    @unpack
    @data(
        ("bar = 1,  # noqa", 0),
        ("bar = 1, 2", 0),
        ("foo = 1", 0),
        ("foo = (1,)", 0),
        ("foo = 1,", 1),
        ("bar = 1; foo = bar,", 1),
        ("foo = (\n3,\n4,\n)\nbar = 10,", 1),
        ("foo = 3,\nbar = 10,\nfoo_bar = 2,", 3),
        ("foo = 3,\nbar = 10 \nfoo_bar = 2,", 2),
        ("foo = 3,\nbar = 10,\nfoo_bar = 2",  2),  # noqa
        ("foo = 3 \nbar = 10 \nfoo_bar = 2,", 1),
        ("class A(object):\n foo = 3\n bar = 10,\n foo_bar = 2", 1),  # noqa
    )
    def test_tuple(self, code, errors):
        result = check_code_for_wrong_tuple(code)
        self.assertEqual(len(result), errors)