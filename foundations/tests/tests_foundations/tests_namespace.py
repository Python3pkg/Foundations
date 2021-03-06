#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_namespace.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`foundations.namespace` module.

**Others:**

"""



import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import foundations.namespace

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["TestSetNamespace",
           "TestGetNamespace",
           "TestRemoveNamespace",
           "TestGetRoot",
           "TestGetLeaf"]


class TestSetNamespace(unittest.TestCase):
    """
    Defines :func:`foundations.namespace.set_namespace` definition units tests methods.
    """

    def test_set_namespace(self):
        """
        Tests :func:`foundations.namespace.set_namespace` definition.
        """

        self.assertIsInstance(foundations.namespace.set_namespace("Namespace", "Attribute"), str)
        self.assertEqual(foundations.namespace.set_namespace("Namespace", "Attribute"), "Namespace|Attribute")
        self.assertEqual(foundations.namespace.set_namespace("Namespace", "Attribute", ":"), "Namespace:Attribute")


class TestGetNamespace(unittest.TestCase):
    """
    Defines :func:`foundations.namespace.get_namespace` definition units tests methods.
    """

    def test_get_namespace(self):
        """
        Tests :func:`foundations.namespace.get_namespace` definition.
        """

        self.assertIsInstance(foundations.namespace.get_namespace("Namespace:Attribute", ":"), str)
        self.assertEqual(foundations.namespace.get_namespace("Namespace|Attribute"), "Namespace")
        self.assertEqual(foundations.namespace.get_namespace("Namespace:Attribute", ":"), "Namespace")
        self.assertEqual(foundations.namespace.get_namespace("Namespace|Attribute|Value", root_only=True), "Namespace")
        self.assertIsNone(foundations.namespace.get_namespace("Namespace"))


class TestRemoveNamespace(unittest.TestCase):
    """
    Defines :func:`foundations.namespace.remove_namespace` definition units tests methods.
    """

    def test_remove_namespace(self):
        """
        Tests :func:`foundations.namespace.remove_namespace` definition.
        """

        self.assertIsInstance(foundations.namespace.remove_namespace("Namespace|Attribute"), str)
        self.assertEqual(foundations.namespace.remove_namespace("Namespace|Attribute"), "Attribute")
        self.assertEqual(foundations.namespace.remove_namespace("Namespace:Attribute", ":"), "Attribute")
        self.assertEqual(foundations.namespace.remove_namespace("Namespace|Attribute|Value"), "Value")
        self.assertEqual(foundations.namespace.remove_namespace(
            "Namespace|Attribute|Value", root_only=True), "Attribute|Value")


class TestGetRoot(unittest.TestCase):
    """
    Defines :func:`foundations.namespace.get_root` definition units tests methods.
    """

    def test_get_root(self):
        """
        Tests :func:`foundations.namespace.get_root` definition.
        """

        self.assertEqual(foundations.namespace.get_root("Attribute"), None)
        self.assertEqual(foundations.namespace.get_root("Namespace|Attribute"), "Namespace")
        self.assertEqual(foundations.namespace.get_root("Namespace:Attribute", ":"), "Namespace")


class TestGetLeaf(unittest.TestCase):
    """
    Defines :func:`foundations.namespace.get_leaf` definition units tests methods.
    """

    def test_get_leaf(self):
        """
        Tests :func:`foundations.namespace.get_leaf` definition.
        """

        self.assertEqual(foundations.namespace.get_leaf("Attribute"), "Attribute")
        self.assertEqual(foundations.namespace.get_leaf("Namespace|Attribute"), "Attribute")
        self.assertEqual(foundations.namespace.get_leaf("Namespace:Attribute", ":"), "Attribute")


if __name__ == "__main__":
    import foundations.tests.utilities

    unittest.main()
