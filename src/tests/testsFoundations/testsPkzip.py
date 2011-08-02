#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**testsPkzip.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Pkzip tests Module.

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
from foundations.pkzip import Pkzip

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
TEST_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.zip")
TREE_HIERARCHY = ("level_0", "loremIpsum.txt", "standard.ibl", "standard.rc", "standard.sIBLT",
					"level_0/standard.ibl", "level_0/level_1",
					"level_0/level_1/loremIpsum.txt", "level_0/level_1/standard.rc", "level_0/level_1/level_2/",
					"level_0/level_1/level_2/standard.sIBLT")

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class PkzipTestCase(unittest.TestCase):
	"""
	This class is the **PkzipTestCase** class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		zipFile = Pkzip(TEST_FILE)
		requiredAttributes = ("archive",)

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(zipFile))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		zipFile = Pkzip(TEST_FILE)
		requiredMethods = ("extract",)

		for method in requiredMethods:
			self.assertIn(method, dir(zipFile))

	def testRead(self):
		"""
		This method tests **Pkzip** class **extract** method.
		"""

		zipFile = Pkzip(TEST_FILE)
		tempDirectory = tempfile.mkdtemp()
		extractionSuccess = zipFile.extract(tempDirectory)
		self.assertTrue(extractionSuccess)
		for item in TREE_HIERARCHY:
			self.assertTrue(os.path.exists(os.path.join(tempDirectory, item)))
		shutil.rmtree(tempDirectory)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

