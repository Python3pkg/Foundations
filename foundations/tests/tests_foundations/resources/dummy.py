#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**dummy.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines helpers objects for **Foundations** package units tests.

**Others:**

"""



import foundations.trace

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["GLOBAL_RETURN_VALUE",
           "Dummy",
           "dummy1",
           "dummy2",
           "dummy3"]

GLOBAL_RETURN_VALUE = list(range(10))


class Dummy(object):
    """
    Defines a dummy class mainly used to test :mod:`foundations.trace` module.
    """

    def __init__(self):
        self.__attribute = GLOBAL_RETURN_VALUE

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        self.__attribute = value

    @attribute.deleter
    def attribute(self):
        return

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __private_method(self):
        return self.__private_method.__name__

    def public_method(self):
        return self.public_method.__name__

    @foundations.trace.untracable
    def untraced_public(self):
        return self.untraced_public.__name__

    @staticmethod
    def static_method():
        return Dummy.static_method.__name__

    @classmethod
    def class_method(cls):
        return cls.class_method.__name__


def dummy1():
    return GLOBAL_RETURN_VALUE


@foundations.trace.untracable
def dummy2():
    return GLOBAL_RETURN_VALUE


def dummy3():
    return GLOBAL_RETURN_VALUE
