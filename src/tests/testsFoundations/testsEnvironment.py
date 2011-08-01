#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsEnvironment.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Environment tests Module.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import os
import platform
import unittest

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
from foundations.environment import Environment

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class EnvironmentTestCase(unittest.TestCase):
	"""
	This class is the EnvironmentTestCase class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		environment = Environment()
		requiredAttributes = ("variables",)

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(environment))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		environment = Environment()
		requiredMethods = ("getValues",
						"setValues")

		for method in requiredMethods:
			self.assertIn(method, dir(environment))

	def testGetValues(self):
		"""
		This method tests the "Environment" class "getValues" method.
		"""

		if platform.system() == "Windows" or platform.system() == "Microsoft":
			environment = Environment("APPDATA")
		elif platform.system() == "Darwin":
			environment = Environment("HOME")
		elif platform.system() == "Linux":
			environment = Environment("HOME")
		self.assertIsInstance(environment.getValues(), dict)
		self.assertIsInstance(environment.getValues("HOME"), dict)
		self.assertIsInstance(environment.getValues().get("HOME"), str)
		self.assertEqual(environment.getValues()["HOME"], os.environ["HOME"])
		environment.getValues("JOHNDOE_IS_FOR_SURE_A_NON_EXISTING_SYSTEM_ENVIRONMENT_VARIABLE")
		self.assertFalse(environment.getValues()["JOHNDOE_IS_FOR_SURE_A_NON_EXISTING_SYSTEM_ENVIRONMENT_VARIABLE"])

	def testSetValues(self):
		"""
		This method tests the "Environment" class "setValues" method.
		"""

		environment = Environment()
		self.assertTrue(environment.setValues(JOHN="DOE"))
		self.assertIn("JOHN", os.environ)
		self.assertTrue(environment.setValues(JOHN="EOD", DOE="JOHN"))
		self.assertIn("DOE", os.environ)
		self.assertEqual(environment.getValues()["JOHN"], "EOD")

	def testGetValue(self):
		"""
		This method tests the "Environment" class "getValue" method.
		"""

		if platform.system() == "Windows" or platform.system() == "Microsoft":
			environment = Environment("APPDATA")
		elif platform.system() == "Darwin":
			environment = Environment("HOME")
		elif platform.system() == "Linux":
			environment = Environment("HOME")
		self.assertTrue(environment.getValue())
		self.assertIsInstance(environment.getValue(), str)
		environment.setValues(JOHN="DOE")
		self.assertEqual(environment.getValue("JOHN"), "DOE")
		self.assertFalse(environment.getValue("JOHNDOE_IS_FOR_SURE_A_NON_EXISTING_SYSTEM_ENVIRONMENT_VARIABLE"))

	def testSetValue(self):
		"""
		This method tests the "Environment" class "setValue" method.
		"""

		environment = Environment()
		self.assertTrue(environment.setValue("JANE", "DOE"))
		self.assertIn("JANE", os.environ)
		self.assertEqual(environment.getValue("JANE"), "DOE")

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

