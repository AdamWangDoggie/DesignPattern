"""
FlyWeight Pattern.
When a program needs to create a lot of similar objects, the cost of memo and calculation would be great.
Use Flyweight Pattern to make objects Share Sources like data with others, instead of duplicate storage or calculating. 
"""

import ramdom
from enum import Enum

TreeType = Enum('Treetype', 'apple_tree cherry_tree peach_tree')

class Tree:
	pool = dict()

	# Use __new__ method to make Tree a Metaclass.(Not a proper describe)
	# But the __new__ method is not for dynamic creating a class.
	# Instead it controls how to create an instance, and still fucking useful.
	# It called object.__new__(cls), to make an instance of cls, the tree.
	def __new__(cls, tree_type):
		obj = cls.pool.get(tree_type, None)
		if not obj:
			obj = object.__new__(cls)
			cls.pool[tree_type] = obj
			obj.tree_type = tree_type
		return obj

	def render(self, age, x, y):
		print('render a tree of type {0} and age {1} at ({2}, {3})'.format(self.tree_type, age, x, y))

def main():
	rnd = random.Random()
	age_min, age_max = 1, 30 # age of the tree
	min_point, max_point = 0, 100  # location of the tree
	tree_counter = 0

	# 10 apple_trees
	for _ in range(10):
		t1 = Tree(TreeType.apple_tree)
		t1.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	# 3 cherry_trees
	for _ in range(3):
		t2 = Tree(TreeType.cherry_tree)
		t2.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	# 5 peach_trees
	for _ in range(5):
		t3 = Tree(TreeType.peach_tree)
		t3.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	print('trees rendered: {}'.format(tree_counter))
	print('trees actually created: {}'.format(len(Tree.pool)))

	t4 = Tree(TreeType.cherry_tree)
	t5 = Tree(TreeType.cherry_tree)
	t6 = Tree(TreeType.apple_tree)
	print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
	print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == "__main__":
	main()

"""
Explaination of the sample above:
Tree.pool, as a dict, contains an instance for each treetype.
When trying to create a tree, the method __new__ will return the existing instance if this treetype had been created.
So every type of tree only has one instance.
When render, the age and location are defined in time.


CONCLUSION
The core thought of Flyweight Pattern:
When you need a lot of objects, 
	1. Share the common attrs by use the same instance(instead of creating as many as you want);
	2. Generate the varying attrs when u need (But not put it in the instance to keep the instance reusable.) 


About method __new__ and __init__:
When you are trying to make a instance of a class, __new__ would be called first and then __init__.
The method __new__ decide how to create the instance(with no attr), __init__ decide how to build(with attrs) the instance(returned by __new__) as its name.
If method __new__ is not defined in your class, it returns object.__new__(cls) by default.


Additon:
You can even return an instance of an other class by define method __new__ in some odd way.

As for real Metaclass, define __new__ in metaclass(The creater), and __metaclass__ in created class.
tips: object.__new__ return an instance, type.__new__ will return a new class.
"""