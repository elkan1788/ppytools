# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

import functools
import logging
import timeit

logger = logging.getLogger(__name__)


def timeMeter(msg=None):
    """Timer meter

        Use this annotation method can calculate the execute time.
    :param msg: custom message output
    :return: fn values
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
                logger.info('Execute <%s.%s> method cost %s seconds.', fn.__module__, fn.__name__, cost)
            return result
        return _wrapper
    return _time_meter