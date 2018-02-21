# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'


class Strings(object):
    """Strings
    """
    def __init__(self):
        pass

    @staticmethod
    def equals(s1, s2):
        return s2 is None if s1 is None else s1 == s2

    @staticmethod
    def equalsIgnoreCase(s1, s2):
        return s2 is None if s1 is None else s1.lower() == s2.lower()
