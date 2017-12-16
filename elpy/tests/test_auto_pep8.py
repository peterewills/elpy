# coding: utf-8

"""Tests for the elpy.autopep8 module"""

import unittest

from elpy import auto_pep8
from elpy.rpc import Fault
from elpy.tests.support import BackendTestCase


class Autopep8TestCase(BackendTestCase):

    def setUp(self):
        if not auto_pep8.autopep8:
            raise unittest.SkipTest

    def test_fix_code(self):
        code_block = 'x=       123\n'
        new_block = auto_pep8.fix_code(code_block)
        self.assertEqual(new_block, 'x = 123\n')

    def test_should_raise_error_when_not_installed(self):
        autopep8_module = auto_pep8.autopep8
        auto_pep8.autopep8 = None
        with self.assertRaises(Fault):
            code_block = 'x=       123\n'
            auto_pep8.fix_code(code_block)
        auto_pep8.autopep8 = autopep8_module
