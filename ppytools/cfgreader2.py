# -*- coding: utf-8 -*-
# __author__ = elkan1788@gmail.com

from ppytools.cfgreader import ConfReader

import ConfigParser
import logging

logger = logging.getLogger(__name__)


class ConfReader2(ConfReader):
    """
    Configure files reader implement under python2 environment.
    """

    def __init__(self, *paths):
        if paths is None or (not paths):
            raise ValueError('Config file paths is required!!!')

        self.cp = ConfigParser.ConfigParser()
        logger.debug('Found %d items config file.', len(paths))
        result = self.cp.read(paths)
        if len(result) != len(result):
            err_cfs = list(set(paths).difference(set(result)))
            logger.error('Found %d config files were uncorrected, See below:', len(err_cfs))
            for path in err_cfs:
                logger.error(path)

        self.values = dict()
        self.__set_values__()
