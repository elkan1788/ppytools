# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.lang import strings

import unittest


class TestStringsCase(unittest.TestCase):

    def testEquals(self):
        self.assertIs(True, strings.equals('String', 'String'))

    def testEqualsIgnore(self):
        self.assertIs(True, strings.equalsignore('String', 'string'))
