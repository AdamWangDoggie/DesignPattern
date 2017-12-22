"""
Command Pattern,
Encapsulate an operation to an object(in python it's class).
Then it can be executed, undid, and other method.
So an operantion can be created intime but execute later, can be redone,
even several operations can be organized as macro to execute in a row
"""

import os

# use verbose to control if msgs would be printed.
verbose = True

class RenameFile:
	def __init__(self, path_src, path_dest):
		self.src, self.dest = path_src, path_dest

	def execute(self):
		if verbose:
			print("[renaming '{}' to '{}']".format(self.src, self.dest))
		os.rename(self.src, self.dest)

	def undo(self):
		if verbose:
			print("[renaming '{}' back to '{}']".format(self.src, self.dest))
		os.rename(self.dest, self.src)