# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'


def equals(s1, s2):
    """Equals 2 string parameters is true or false

    :param s1:
    :param s2:
    :return:
    """
    return s2 is None if s1 is None else s1 == s2

def equalsignore(s1, s2):
    """Equals 2 string parameters is true or false without word upper or lower

    :param s1:
    :param s2:
    :return:
    """
    return s2 is None if s1 is None else s1.lower() == s2.lower()
