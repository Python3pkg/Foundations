#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**common.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Foundations** package common utilities objects that don't fall in any specific category.

**Others:**
	:func:`isBinaryFile` from Jorge Orpinel:
	http://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
	:func:`dependencyResolver` from Louis Riviere: http://code.activestate.com/recipes/576570-dependency-resolver/

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import itertools
import os
import socket
import urllib2

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.verbose

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2013 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER",
		"CONNECTION_IP",
		"DEFAULT_HOST_IP",
		"wait",
		"uniqify",
		"unpackDefault",
		"orderedUniqify",
		"pathExists",
		"filterPath",
		"getFirstItem",
		"getLastItem",
		"isBinaryFile",
		"repeat",
		"dependencyResolver",
		"isInternetAvailable",
		"getHostAddress"]

LOGGER = foundations.verbose.installLogger()

CONNECTION_IP = "www.google.com"
DEFAULT_HOST_IP = "127.0.0.1"

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
def uniqify(sequence):
	"""
	This definition uniqifies the given sequence even if unhashable.

	:param sequence: Sequence.
	:type sequence: object
	:return: Uniqified sequence.
	:rtype: list
	
	:note: The sequence order is not maintained by this definition.
	"""

	return [key for key, group in itertools.groupby(sorted(sequence))]

def orderedUniqify(sequence):
	"""
	This definition uniqifies the given hashable sequence while preserving its order.

	:param sequence: Sequence.
	:type sequence: object
	:return: Uniqified sequence.
	:rtype: list
	"""

	items = set()
	return [key for key in sequence if key not in items and not items.add(key)]

def unpackDefault(iterable, length=3, default=None):
	"""
	This definition unpacks given iterable maintaining given length and filling missing entries with given default.

	:param iterable: iterable.
	:type iterable: object
	:param length: Iterable length.
	:type length: int
	:param default: Filling default object.
	:type default: object
	:return: Unpacked iterable.
	:rtype: object
	"""

	return itertools.islice(itertools.chain(iter(iterable), itertools.repeat(default)), length)

def pathExists(path):
	"""
	This definition returns if given path exists.

	:param path: Path.
	:type path: unicode
	:return: Path existence.
	:rtype: bool
	"""

	if not path:
		return False
	else:
		return os.path.exists(path)

def filterPath(path):
	"""
	This definition filters given path.

	:param path: Path.
	:type path: unicode
	:return: Filtered path.
	:rtype: unicode
	"""

	return path if pathExists(path) else ""

def getFirstItem(iterable, default=None):
	"""
	This definition returns the first item of given iterable.

	:param iterable: Iterable.
	:type iterable: object
	:param default: Default value.
	:type default: object
	:return: First iterable item.
	:rtype: object
	"""

	if not iterable:
		return default

	for item in iterable:
		return item

def getLastItem(iterable, default=None):
	"""
	This definition returns the last item of given iterable.

	:param iterable: Iterable.
	:type iterable: object
	:param default: Default value.
	:type default: object
	:return: Last iterable item.
	:rtype: object
	"""

	if not iterable:
		return default

	return iterable[-1]

def isBinaryFile(file):
	"""
	This definition returns if given file is a binary file.

	:param file: File path.
	:type file: unicode
	:return: Is file binary.
	:rtype: bool
	"""

	fileHandle = open(file, "rb")
	try:
		chunkSize = 1024
		while True:
			chunk = fileHandle.read(chunkSize)
			if chr(0) in chunk:
				return True
			if len(chunk) < chunkSize:
				break
	finally:
		fileHandle.close()
	return False

def repeat(object, iterations=1):
	"""
	This definition repeats given object iterations times.

	:param object: Object to repeat.
	:type object: object
	:param iterations: Repetitions number.
	:type iterations: int
	:return: Object return values.
	:rtype: list
	"""

	return [object() for i in range(iterations)]

def dependencyResolver(dependencies):
	"""
	This definition resolves given dependencies.

	:param dependencies: Dependencies to resolve.
	:type dependencies: dict
	:return: Resolved dependencies.
	:rtype: list
	"""

	items = dict((key, set(dependencies[key])) for key in dependencies)
	resolvedDependencies = []
	while items:
		batch = set(item for value in items.values() for item in value) - set(items.keys())
		batch.update(key for key, value in items.items() if not value)
		resolvedDependencies.append(batch)
		items = dict(((key, value - batch) for key, value in items.items() if value))
	return resolvedDependencies

def isInternetAvailable(ip=CONNECTION_IP, timeout=1.5):
	"""
	This definition returns if an internet connection is available.

	:param ip: Alternative address ip to check against.
	:type ip: unicode
	:param timeout: Timeout in seconds.
	:type timeout: int
	:return: Is internet available.
	:rtype: bool
	"""

	try:
		urllib2.urlopen("http://{0}".format(ip), timeout=timeout)
		return True
	except (urllib2.URLError, socket.error) as error:
		return False

def getHostAddress(host=None, defaultAddress=DEFAULT_HOST_IP):
	"""
	This definition returns the given host address.

	:param host: Host to retrieve the address.
	:type host: unicode
	:param defaultAddress: Default address if the host is unreachable.
	:type defaultAddress: unicode
	:return: Host address.
	:rtype: unicode
	"""

	try:
		return unicode(socket.gethostbyname(host or socket.gethostname()))
	except Exception as error:
		return defaultAddress
