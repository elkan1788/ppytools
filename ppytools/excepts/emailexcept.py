# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'


class EmailException(Exception):
    """EmailException
    """
    def __init__(self, err='An email exception.'):
        Exception.__init__(self, err)


class SendEmailException(EmailException):
    """SendEmailException
    """
    def __init__(self, err='Send email exception.'):
        EmailException.__init__(self, err)


class AppendEmailAttException(EmailException):
    """AppendEmailAttException
    """
    def __init__(self, err='Append email attachment exception.'):
        EmailException.__init__(self, err)


class DeleteEmailAttException(EmailException):
    """DeleteEmailAttException
    """
    def __init__(self, err='Delete email attachment exception.'):
        EmailException.__init__(self, err)





