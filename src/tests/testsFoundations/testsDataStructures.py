#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsDataStructures.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`foundations.dataStructures` module.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import unittest

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.dataStructures

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["NestedAttributeTestCase",
			"StructureTestCase",
			"OrderedStructureTestCase",
			"LookupTestCase"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class NestedAttributeTestCase(unittest.TestCase):
	"""
	This class defines :class:`foundations.dataStructures.NestedAttribute` class units tests methods.
	"""

	def testNestedAttribute(self):
		"""
		This method tests :class:`foundations.dataStructures.NestedAttribute` class.
		"""

		nest = foundations.dataStructures.NestedAttribute()
		nest.my.deeply.nested.attribute = 64
		self.assertTrue(hasattr(nest, "nest.my.deeply.nested.attribute"))
		self.assertEqual(nest.my.deeply.nested.attribute, 64)

class StructureTestCase(unittest.TestCase):
	"""
	This class defines :class:`foundations.dataStructures.Structure` class units tests methods.
	"""

	def testStructure(self):
		"""
		This method tests :class:`foundations.dataStructures.Structure` class.
		"""

		structure = foundations.dataStructures.Structure(John="Doe", Jane="Doe")
		self.assertIn("John", structure.keys())
		self.assertTrue(hasattr(structure, "John"))

class OrderedStructureTestCase(unittest.TestCase):
	"""
	This class defines :class:`foundations.dataStructures.OrderedStructure` class units tests methods.
	"""

	def testOrderedStructure(self):
		"""
		This method tests :class:`foundations.dataStructures.OrderedStructure` class.
		"""

		structure = foundations.dataStructures.OrderedStructure([("personA", "John"), ("personB", "Jane"), ("personC", "Luke")])
		self.assertIn("personA", structure.keys())
		self.assertTrue(hasattr(structure, "personA"))
		self.assertListEqual(["personA", "personB", "personC"], structure.keys())
		structure["personA"] = "Anakin"
		self.assertEquals("Anakin", structure.personA)
		structure.personA = "John"
		self.assertEquals("John", structure["personA"])
		del(structure.personA)
		self.assertTrue("personA" not in structure.keys())
		del(structure["personB"])
		self.assertTrue(not hasattr(structure, "personB"))

class LookupTestCase(unittest.TestCase):
	"""
	This class defines :class:`foundations.dataStructures.Lookup` class units tests methods.
	"""

	def testGetFirstKeyFromValue(self):
		"""
		This method tests :meth:`foundations.dataStructures.Lookup.getFirstKeyFromValue` method.
		"""

		lookup = foundations.dataStructures.Lookup(firstName="Doe", lastName="John", gender="male")
		self.assertEqual("firstName", lookup.getFirstKeyFromValue("Doe"))

	def testGetKeysFromValue(self):
		"""
		This method tests :meth:`foundations.dataStructures.Lookup.getKeysFromValue` method.
		"""

		lookup = foundations.dataStructures.Lookup(John="Doe", Jane="Doe", Luke="Skywalker")
		self.assertListEqual(["Jane", "John"], lookup.getKeysFromValue("Doe"))

if __name__ == "__main__":
	unittest.main()