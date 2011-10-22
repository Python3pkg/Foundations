#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**dag.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines various dag related class.

**Others:**
	Portions of the code from DAG by Simon Wittber: http://pypi.python.org/pypi/DAG/ and PyQt4 Model View Programming Tutorials by Yasin Uludag: http://www.yasinuludag.com/blog/?p=98
"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import logging
import weakref

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
from foundations.globals.constants import Constants

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "Attribute", "AbstractNode", "AbstractCompositeNode"]

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class Attribute(core.Structure):
	"""
	This class represents a storage object for the :class:`AbstractNode` class attributes.
	"""

	@core.executionTrace
	def __init__(self, **kwargs):
		"""
		This method initializes the class.

		:param \*\*kwargs: value, image. ( Key / Value pairs )
		"""

		core.Structure.__init__(self, **kwargs)

class AbstractNode(core.Structure):
	"""
	| This class defines the base node class.
	| Although it can be instancied directly that class is meant to be subclassed.
	
	:note: This class doesn't provide compositing capabilities, class:`AbstractCompositeNode` class must be used for that purpose.
	"""

	__family = "Abstract"
	"""Node family. ( String )"""

	__instanceId = 1
	"""Node id: Defines the next node instance identity number. ( Integer )"""

	__nodesInstances = weakref.WeakValueDictionary()
	"""Node instances: Each node, once instanced is stored in this attribute. ( Dictionary )"""

	@core.executionTrace
	def __new__(self, *args, **kwargs):
		"""
		This method is the constructor of the class.
		
		:param \*args: Arguments. ( \* )
		:param \*\*kwargs: Keywords arguments. ( \* )
		:return: Class instance. ( AbstractNode )
		"""

		instance = super(AbstractNode, self).__new__(self)
		instance.__identity = AbstractNode._AbstractNode__instanceId
		AbstractNode._AbstractNode__nodesInstances[instance.__identity] = instance
		AbstractNode._AbstractNode__instanceId += 1
		return instance

	@core.executionTrace
	def __init__(self, name=None, **kwargs):
		"""
		This method initializes the class.

		Usage::

			>>> nodeA = AbstractNode("MyNodeA")
			>>> nodeA.identity
			1
			>>> nodeB = AbstractNode()
			>>> nodeB.name
			'Abstract2'
			>>> nodeB.identity
			2

		:param name: Node name.  ( String )
		:param \*\*kwargs: Keywords arguments. ( \* )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		core.Structure.__init__(self, **kwargs)

		# --- Setting class attributes. ---
		self.__name = None
		self.__name = name or self.__getDefaultNodeName()

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def family(self):
		"""
		This method is the property for **self.__family** attribute.

		:return: self.__family. ( String )
		"""

		return getattr(self, "_{0}__{1}".format(self.__class__.__name__, "family"))

	@family.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def family(self, value):
		"""
		This method is the setter method for **self.__family** attribute.

		:param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "family"))

	@family.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def family(self):
		"""
		This method is the deleter method for **self.__family** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "family"))

	@property
	def nodesInstances(self):
		"""
		This method is the property for **self.__nodesInstances** attribute.

		:return: self.__nodesInstances. ( WeakValueDictionary )
		"""

		return self.__nodesInstances

	@nodesInstances.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def nodesInstances(self, value):
		"""
		This method is the setter method for **self.__nodesInstances** attribute.

		:param value: Attribute value. ( WeakValueDictionary )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "nodesInstances"))

	@nodesInstances.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def nodesInstances(self):
		"""
		This method is the deleter method for **self.__nodesInstances** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "nodesInstances"))

	@property
	def identity(self):
		"""
		This method is the property for **self.__identity** attribute.

		:return: self.__identity. ( String )
		"""

		return self.__identity

	@identity.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def identity(self, value):
		"""
		This method is the setter method for **self.__identity** attribute.

		:param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "identity"))

	@identity.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def identity(self):
		"""
		This method is the deleter method for **self.__identity** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "identity"))

	@property
	def name(self):
		"""
		This method is the property for **self.__name** attribute.

		:return: self.__name. ( String )
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self, value):
		"""
		This method is the setter method for **self.__name** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		This method is the deleter method for **self.__name** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "name"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	def __repr__(self):
		"""
		This method reimplements the :meth:`core.Structure.__repr__` method.
		
		:return: Object representation. ( String )
		"""

		return "<{0} object at {1}>".format(self.__class__.__name__, hex(id(self)))

	@core.executionTrace
	def __getDefaultNodeName(self):
		"""
		This method gets the default node name.
		
		:return: Node name. ( String )
		"""

		return "{0}{1}".format(self.family, self.__identity)

	@classmethod
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def getNodeByIdentity(self, identity):
		"""
		This method returns the node with provided identity.
	
		Usage::

			>>> nodeA = AbstractNode("MyNodeA")
			>>> AbstractNode.getNodeByIdentity(1)
			<AbstractNode object at 0x101043a80>

		:param identity: Node identity. ( Integer )
		:return: Node. ( AbstractNode )

		:note: Nodes identities are starting from '1' to nodes instances count.
		"""

		if identity < 1 or identity > len(self.__nodesInstances):
			return
		return self.__nodesInstances[identity]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def listAttributes(self):
		"""
		This method returns the node attributes names.

		Usage::

			>>>	nodeA = AbstractNode("MyNodeA", attributeA=Attribute(value="A"), attributeB=Attribute(value="B"))
			>>> nodeA.listAttributes()
			['attributeB', 'attributeA']
			
		:return: Attributes names. ( List )
		"""

		return [attribute for attribute, value in self.items() if isinstance(value, Attribute)]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def getAttributes(self):
		"""
		This method returns the node attributes.

		Usage::

			>>>	nodeA = AbstractNode("MyNodeA", attributeA=Attribute(), attributeB=Attribute())
			>>> nodeA.getAttributes()
			[{'value': 'B'}, {'value': 'A'}]

		:return: Attributes. ( List )
		"""

		return [attribute for attribute in self.values() if isinstance(attribute, Attribute)]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def attributeExists(self, name):
		"""
		This method returns if provided attribute exists in the node.

		Usage::

			>>>	nodeA = AbstractNode("MyNodeA", attributeA=Attribute(), attributeB=Attribute())
			>>> nodeA.attributeExists("attributeA")
			True
			>>> nodeA.attributeExists("attributeC")
			False

		:param name: Attribute name. ( String )
		:return: Attribute exists. ( Boolean )
		"""

		if name in self.keys():
			if isinstance(self[name], Attribute):
				return True
		return False

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.NodeAttributeTypeError)
	def addAttribute(self, name, value):
		"""
		This method adds provided attribute to the node.

		Usage::

			>>>	nodeA = AbstractNode()
			>>> nodeA.addAttribute("attributeA", Attribute(value="A"))
			True
			>>> nodeA.listAttributes()
			['attributeA']
	
		:param name: Attribute name. ( String )
		:param value: Attribute value. ( Attribute )
		:return: Method success. ( Boolean )
		"""

		if not isinstance(value, Attribute):
			raise foundations.exceptions.NodeAttributeTypeError("Node attribute value must be a '{0}' class instance!".format(Attribute.__class__.__name__))

		if self.attributeExists(name):
			raise foundations.exceptions.NodeAttributeExistsError("Node attribute '{0}' already exists!".format(name))

		self[name] = value
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.NodeAttributeExistsError)
	def removeAttribute(self, name):
		"""
		This method removes provided attribute from the node.

		Usage::

			>>>	nodeA = AbstractNode("MyNodeA", attributeA=Attribute(), attributeB=Attribute())
			>>> nodeA.removeAttribute("attributeA")
			True
			>>> nodeA.listAttributes()
			['attributeB']

		:param name: Attribute name. ( String )
		:return: Method success. ( Boolean )
		"""

		if not self.attributeExists(name):
			raise foundations.exceptions.NodeAttributeExistsError("Node attribute '{0}' doesn't exists!".format(name))

		del self[name]
		return True

class AbstractCompositeNode(AbstractNode):
	"""
	| This class defines the base composite node class.
	| It provides compositing capabilities allowing the assembly of graphs and various trees structures.
	"""

	__family = "AbstractComposite"

	@core.executionTrace
	def __init__(self, name=None, parent=None, children=None, **kwargs):
		"""
		This method initializes the class.

		:param name: Node name.  ( String )
		:param parent: Node parent. ( AbstractNode / AbstractCompositeNode )
		:param children: Children. ( List )
		:param \*\*kwargs: Keywords arguments. ( \* )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		AbstractNode.__init__(self, name, **kwargs)

		# --- Setting class attributes. ---
		self.__parent = None
		self.parent = parent
		self.__children = children or []

		parent and parent.addChild(self)

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def parent(self):
		"""
		This method is the property for **self.__parent** attribute.

		:return: self.__parent. ( QObject )
		"""

		return self.__parent

	@parent.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def parent(self, value):
		"""
		This method is the setter method for **self.__parent** attribute.

		:param value: Attribute value. ( QObject )
		"""

		if value:
			assert issubclass(value.__class__, AbstractNode), "'{0}' attribute: '{1}' is not a '{2}' subclass!".format("parent", value, AbstractNode.__class__.__name__)
		self.__parent = value

	@parent.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def parent(self):
		"""
		This method is the deleter method for **self.__parent** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "name"))

	@property
	def children(self):
		"""
		This method is the property for **self.__children** attribute.

		:return: self.__children. ( QObject )
		"""

		return self.__children

	@children.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def children(self, value):
		"""
		This method is the setter method for **self.__children** attribute.

		:param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "children"))

	@children.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def children(self):
		"""
		This method is the deleter method for **self.__children** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "children"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def child(self, index):
		"""
		This method returns the child associated with given index.
	
		:param index: Child index. ( Integer )
		:return: Child node. ( AbstractNode / AbstractCompositeNode / Object )
		"""

		if index >= 0 or index <= len(self.__children):
			return self.__children[index]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def indexOf(self, child):
		"""
		This method returns the given child index.
	
		:param child: Child node. ( AbstractNode / AbstractCompositeNode / Object )
		:return: Child index. ( Integer )
		"""

		for i, item in enumerate(self.__children):
			if child is item:
				return i

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def row(self):
		"""
		This method returns the node row.
	
		:return: Node row. ( Integer )
		"""

		if self.__parent:
			return self.__parent.indexOf(self)

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def addChild(self, child):
		"""
		This method adds provided child to the node.
	
		:param child: Child node. ( AbstractNode / AbstractCompositeNode / Object )
		:return: Method success. ( Boolean )
		"""

		self.__children.append(child)
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def removeChild(self, index):
		"""
		This method removes provided index from the node children.
	
		:param index: Node index. ( Integer )
		:return: Method success. ( Boolean )
		"""

		if index < 0 or index > len(self.__children):
			return

		child = self.__children.pop(index)
		child.__parent = None
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def insertChild(self, child, index):
		"""
		This method inserts provided child at given index.
	
		:param child: Child node. ( AbstractNode / AbstractCompositeNode / Object )
		:param index: Insertion index. ( Integer )
		:return: Method success. ( Boolean )
		"""

		if index < 0 or index > len(self.__children):
			return

		self.__children.insert(index, child)
		child.__parent = self
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def childrenCount(self):
		"""
		This method returns the children count.
	
		:return: Children count. ( Integer )
		"""

		return len(self.__children)

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def listNode(self, tabLevel= -1):
		"""
		This method lists the current node and its children.
	
		:return: Node listing. ( String )
		"""

		output = ""
		tabLevel += 1
		for i in range(tabLevel):
			output += "\t"
		output += "|----'{0}'\n".format(self.name)
		for child in self.__children:
			output += child.listNode(tabLevel)
		tabLevel -= 1
		return output