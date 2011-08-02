#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsRotatingBackup.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	RotatingBackup tests Module.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import os
import shutil
import tempfile
import unittest

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
from foundations.rotatingBackup import RotatingBackup

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
TEST_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.ibl")
TEST_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, "standard")

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class RotatingBackupTestCase(unittest.TestCase):
	"""
	This class is the **RotatingBackupTestCase** class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		rotatingBackup = RotatingBackup()
		requiredAttributes = ("source",
							"destination",
							"count")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(rotatingBackup))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		rotatingBackup = RotatingBackup()
		requiredMethods = ("backup", "copy", "delete")

		for method in requiredMethods:
			self.assertIn(method, dir(rotatingBackup))

	def testBackup(self):
		"""
		This method tests **RotatingBackup** class **backup** method.
		"""

		tempDirectory = tempfile.mkdtemp()
		rotatingBackup = RotatingBackup(TEST_FILE, tempDirectory, 3)
		rotatingBackup.backup()
		self.assertTrue(os.path.exists(os.path.join(tempDirectory, os.path.basename(TEST_FILE))))
		for i in range(1, 4):
			rotatingBackup.backup()
			self.assertTrue(os.path.exists(os.path.join(tempDirectory, os.path.basename("{0}.{1}".format(TEST_FILE, i)))))
		rotatingBackup.backup()
		self.assertFalse(os.path.exists(os.path.join(tempDirectory, os.path.basename("{0}.4".format(TEST_FILE)))))
		shutil.rmtree(tempDirectory)

	def testCopy(self):
		"""
		This method tests **RotatingBackup** class **copy** method.
		"""

		tempDirectory = tempfile.mkdtemp()
		rotatingBackup = RotatingBackup(TEST_FILE, tempDirectory, 3)
		for element in (TEST_FILE, TEST_DIRECTORY):
			destination = os.path.join(tempDirectory, os.path.basename(element))
			rotatingBackup.copy(element, destination)
			self.assertTrue(os.path.exists(destination))
		shutil.rmtree(tempDirectory)

	def testDelete(self):
		"""
		This method tests **RotatingBackup** class **delete** method.
		"""

		tempDirectory = tempfile.mkdtemp()
		rotatingBackup = RotatingBackup(TEST_FILE, tempDirectory, 3)
		for element in (TEST_FILE, TEST_DIRECTORY):
			destination = os.path.join(tempDirectory, os.path.basename(element))
			rotatingBackup.copy(element, destination)
			rotatingBackup.delete(destination)
			self.assertTrue(not os.path.exists(destination))
		shutil.rmtree(tempDirectory)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

