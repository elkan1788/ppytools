# coding: utf-8
# __author__ = 'elkan1788@gmail.com'

from ppytools.lang.strings_helper import Strings

import unittest


class TestStringsCase(unittest.TestCase):

    def testEquals(self):
        self.assertIs(True, Strings.equals('String', 'String'))

    def testEqualsIgnoreCase(self):
        self.assertIs(True, Strings.equalsIgnoreCase('String', 'string'))
