"""
Proxy Pattern-LazyProperty.
Use a descriptor as decorator, to lazy init a attr of instance.
Make sense improving performance if initiation of an instance cause great cost.
"""


class LazyProperty:
	def __init__(self, method):
		self.method = method
		self.method_name = method.__name__
		print('function overriden: {}'.format(self.method))
		print("function's name: {}".format(self.method_name))
	def __get__(self, obj, cls):
		print('=============1============')
		print(obj.__dict__)
		if not obj:
			return None
		value = self.method(obj)
		print('value {}'.format(value))
		print(obj.__dict__)
		setattr(obj, self.method_name, value)
		print(obj.__dict__)
		return value


class Test:
	def __init__(self):
		self.x = 'foo'
		self.y = 'bar'
		self._resource = None

	@LazyProperty
	def resource(self):
		print('===========2=============')
		print('initializing self._resource which is: {}'.format(self._resource))
		self._resource = tuple(range(5))
		print('===========3=============')
		return self._resource


def main():
	print('===HO===')
	t = Test()
	print(t.x)
	print(t.y)
	print(t.resource)
	print(t.resource)


if __name__ == "__main__":
	main()