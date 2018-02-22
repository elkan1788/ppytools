# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

import logging

logger = logging.getLogger(__name__)


import timeit
import functools

def timeMeter(msg=None):
    """

    :param msg:
    :return:
    """
    def _time_meter(fn):
        @functools.wraps(fn)
        def _wrapper(*args, **kwargs):
            mark = timeit.default_timer()
            result = fn(*args, **kwargs)
            cost = timeit.default_timer() - mark
            if msg:
                logger.info(msg, cost)
            else:
                logger.info('Execute <%s> method cost %s seconds.', fn.__name__, cost)
            return result
        return _wrapper
    return _time_meter