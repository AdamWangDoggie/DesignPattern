"""
Facade Pattern
Provide an Simple and Brief Interface, to ignore details in bottom.
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')

class User:
	pass


class Process:
	pass


class File:
	pass


# Use ABCMeta as metaclass to make an ABSTRACT CLASS, which cannot instantiate.
class Server(metaclass=ABCMeta):
	# Methods decorated by abstractmethod must be override by subclass.
	@abstractmethod
	def __init__(self):
		pass

	def __str__(self):
		return self.name

	@abstractmethod
	def boot(self):
		pass

	@abstractmethod
	def kill(self, restart=True):
		pass


# Inherit from Server
class FileServer(Server):
	def __init__(self):
		self.name = 'FileServer'
		self.state = State.new

	def boot(self):
		# Start file server
		print('booting the {}'.format(self))
		self.state = State.running

	def kill(self, restart=True):
		# Stop file server
		print('Killing {}'.format(self))
		self.state = State.restart if restart else State.zombie

	def create_file(self, user, name, permissions):
		print("Trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):
	def __init__(self):
		self.name = 'ProcessServer'
		self.state = State.new

	def boot(self):
		print('booting the {}'.format(self))
		self.state = State.new

	def kill(self, restart=True):
		print('Killing {}'.format(self))
		self.state = State.restart if restart else State.zombie

	def create_process(self, user, name):
		print("Trying to create the process '{}' for user '{}'".format(name, user))


class WindowServer:
	pass


class NetworkServer:
	pass


class OperatingSystem:
	# The Facade
	def __init__(self):
		self.fs = FileServer()
		self.ps = ProcessServer()
		#self.ws = WindowServer
		#self.nws = NetworkServer

	def start(self):
		# Boot all server
		for i in (self.fs, self.ps):
			i.boot()

	def create_file(self, user, name, permissions):
		return self.fs.create_file(user, name, permissions)

	def create_process(self, user, name):
		return self.ps.create_process(user, name)


def main():
	os = OperatingSystem()
	os.start()
	os.create_file('foo', 'hello', '-rw-r-r')
	os.create_process('bar', 'ls/tmp')


if __name__ == "__main__":
	main()
	input()

"""
Client can take all actions through only OperatingSystem, and ignore whatever servers.
"""