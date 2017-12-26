"""
Adapter Pattern.
To Adapt or Make APIs Compatible.
"""

class Synthesizer:
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return '<Synthesizer {}>'.format(self.name)

	def play(self):
		return 'Playing a song.'


class Human:
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return '<Human {}>'.format(self.name)

	def speak(self):
		return 'Says hello.'


class Computer:
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return '<Computer {}>'.format(self.name)

	def execute(self):
		return 'Executing a program.'


class Adapter: ### IMPORTANT
	def __init__(self, obj, adapted_methods):
		self.obj = obj
		# self.name = self.obj.name
		self.__dict__.update(self.obj.__dict__)
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)


def main():
	objects = [Computer('Asus')]
	synth = Synthesizer('moog')
	objects.append(Adapter(synth, dict(execute=synth.play)))
	human = Human('Bob')
	objects.append(Adapter(human, dict(execute=human.speak)))

	for i in objects:
		print('{} {}'.format(str(i), i.execute()))
		print(i.name)


if __name__ == "__main__":
	main()
	input()