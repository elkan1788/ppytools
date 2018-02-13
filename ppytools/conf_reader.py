# coding: utf-8
# __author__ = 'elkan1788@gmail.com'

import ConfigParser
import logging
from collections import namedtuple

logger = logging.getLogger(__name__)


class ConfReader(object):
    """Read *.ini config file info as a dict or tuple.

    Attributes:
         cp: ConfigParser object
         values: Sections's value dict
    """

    sections = []

    def __init__(self, *paths):
        """Init config reader
            Read config files's path then put all values into a dict.
            When path not correct will output by logger err.
        :param
            paths: config file paths

        :exception
            ValueError: An error occurred the config file path is none or empty.
        """
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

    def __set_values__(self):
        """Parse all config files's key,value
        """
        sections = self.cp.sections()
        for section in sections:
            self.values[section] = dict()
            options = self.cp.options(section)
            for option in options:
                value = self.cp.get(section, option, 'None')
                self.values[section][option] = value

    def sections(self):
        """Find config files's section name

        :return: all section name
        """
        return self.cp.sections()

    def get_keys(self, section):
        """Get section's keys

        :param section: section name
        :return: section's keys
        """
        return self.cp.options(section)

    def get_all_values(self):
        """Get sections's values

        :return: all sections values dict
        """
        return self.values

    def get_values(self, section):
        """Get section's value

        :param section: section name
        :return: section key and value dict
        """
        return self.values[section]

    def get_value(self, section, key):
        """Get section key value

        :param section: section name
        :param key: key name
        :return: value default is None string
        """
        return self.values[section][key]

    def get_tuple(self, section):
        """Get section name tuple

        :param section: section name
        :return: tuple object
        """
        keys = self.get_keys(section)
        value_dict = self.get_values(section)
        return namedtuple(section, keys)(**value_dict)
