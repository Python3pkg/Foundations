#!/usr/bin/env python
# -*- coding: utf-8 -*-

#***********************************************************************************************
#
# Copyright (C) 2008 - 2011 - Thomas Mansencal - thomas.mansencal@gmail.com
#
#***********************************************************************************************
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************************************
#
# The Following Code Is Protected By GNU GPL V3 Licence.
#
#***********************************************************************************************

"""
************************************************************************************************
***	rotatingBackup.py
***
***	Platform:
***		Windows, Linux, Mac Os X
***
***	Description:
***		Rotating Backup Module.
***
***	Others:
***		Code Extracted From rotatingbackup.py Written By leo.ss.pku@gmail.com
************************************************************************************************
"""

#***********************************************************************************************
#***	Python Begin
#***********************************************************************************************

#***********************************************************************************************
#***	External Imports
#***********************************************************************************************
import logging
import os
import shutil

#***********************************************************************************************
#***	Internal Imports
#***********************************************************************************************
import core
import foundations.exceptions
from globals.constants import Constants

#***********************************************************************************************
#***	Global Variables
#***********************************************************************************************
LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module Classes And Definitions
#***********************************************************************************************
class RotatingBackup(object):
	"""
	This Class Is The RotatingBackup Class.
	"""

	@core.executionTrace
	def __init__(self, source=None, destination=None, count=3):
		"""
		This Method Initializes The Class.

		@param source: Backup Source. ( String )
		@param destination: Backup Destination. ( String )
		@param count: Backup Count. ( Integer )
		"""

		LOGGER.debug("> Initializing '{0}()' Class.".format(self.__class__.__name__))

		# --- Setting Class Attributes. ---
		self._source = None
		self._source = source
		self._destination = None
		self._destination = destination
		self._count = None
		self._count = count

	#***************************************************************************************
	#***	Attributes Properties
	#***************************************************************************************
	@property
	def source(self):
		"""
		This Method Is The Property For The _source Attribute.

		@return: self._source. ( String )
		"""

		return self._source

	@source.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def source(self, value):
		"""
		This Method Is The Setter Method For The _source Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("source", value)
			assert os.path.exists(value), "'{0}' Attribute: '{1}' File Doesn't Exists!".format("source", value)
		self._source = value

	@source.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def source(self):
		"""
		This Method Is The Deleter Method For The _source Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("source"))

	@property
	def destination(self):
		"""
		This Method Is The Property For The _destination Attribute.

		@return: self._destination. ( String )
		"""

		return self._destination

	@destination.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def destination(self, value):
		"""
		This Method Is The Setter Method For The _destination Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("destination", value)
		self._destination = value

	@destination.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def destination(self):
		"""
		This Method Is The Deleter Method For The _destination Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("destination"))

	@property
	def count(self):
		"""
		This Method Is The Property For The _count Attribute.

		@return: self._count. ( Integer )
		"""

		return self._count

	@count.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def count(self, value):
		"""
		This Method Is The Setter Method For The _count Attribute.
		
		@param value: Attribute Value. ( Integer )
		"""

		if value:
			assert type(value) in (int, float), "'{0}' Attribute: '{1}' Type Is Not 'int' or 'float'!".format("count", value)
			assert value > 0, "'{0}' Attribute: '{1}' Need To Be Exactly Positive!".format("count", value)
		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Read Only!".format("count"))

	@count.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def count(self):
		"""
		This Method Is The Deleter Method For The _count Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("count"))

	#***************************************************************************************
	#***	Class Methods
	#***************************************************************************************
	@core.executionTrace
	def backup(self):
		"""
		This Method Does The Rotating Backup.
		"""

		LOGGER.debug("> Storing '{0}' File Backup.".format(self._source))

		if self._source and self._destination:
			os.path.exists(self._destination) or os.mkdir(self._destination)
			destination = os.path.join(self._destination, os.path.basename(self._source))
			for i in range(self._count - 1, 0, -1):
				sfn = "{0}.{1}".format(destination, i)
				dfn = "{0}.{1}".format(destination, i + 1)
				if os.path.exists(sfn):
					if os.path.exists(dfn):
						self.delete(dfn)
					os.renames(sfn, dfn)
			os.path.exists(destination) and os.rename(destination, destination + ".1")
			self.copy(self._source, destination)

	@foundations.exceptions.exceptionsHandler(None, False, OSError)
	@core.executionTrace
	def copy(self, source, destination):
		"""
		This Method Copies The Provided Path To Destination.

		@param source: Source To Copy From. ( String )
		@param destination: Destination To Copy To. ( String )
		"""

		LOGGER.debug("> Copying '{0}' File To '{1}'.".format(source, destination))

		if os.path.isfile(source):
			shutil.copyfile(source, destination)
		else:
			shutil.copytree(source, destination)

	@foundations.exceptions.exceptionsHandler(None, False, OSError)
	@core.executionTrace
	def delete(self, path):
		"""
		This Method Deletes The Provided Resource.

		@param path: Resource To Delete. ( String )
		"""

		LOGGER.debug("> Removing '{0}' File.".format(path))

		if os.path.isfile(path):
			os.remove(path)
		elif os.path.isdir(path):
			shutil.rmtree(path)

#***********************************************************************************************
#***	Python End
#***********************************************************************************************
