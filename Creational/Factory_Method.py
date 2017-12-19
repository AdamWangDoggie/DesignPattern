"""
Factory Method, one of factory pattern.

"""

import xml.etree.ElementTree as etree
import json

class JSONConnector:
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, method='r', encoding='utf-8') as f:
			self.data = json.load(f)

	@property
	def parsed_data(self):
		return self.data


class XMLConnector:
	def __init__(self, filepath):
		self.tree = etree.parse(filepath)

	@property
	def parsed_data(self):
		return self.tree


def connection_factory(filepath):
	if filepath.endswith('json'):
		connector = JSONConnector
	elif filepath.endswith('xml'):
		connector = XMLConnector
	else:
		raise ValueError('Cannot connect to {}'.format(filepath))
	return connector(filepath)


def connect_to(filepath):
	factory = None
	try:
		factory = connection_factory(filepath)
	except ValueError as ve:
		print(ve)
	return factory

"""
1. JSONConnector and XMLConnector deal with specific file, xml or json.
2. Connection_factory abstract from above two connector, user can ignore file type through this.
3. Abstract more, provide a simple interface, user just call one func and catch exception. 
*. Exception catch can be more ignored, just print the error in connection_factory.
"""