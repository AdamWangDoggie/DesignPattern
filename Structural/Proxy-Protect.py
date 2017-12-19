"""
Proxy Pattern-Protection.
Use proxy pattern to protect sensitive info.
Client should access proxy instead of the info itself, and the proxy 
provide validation to protect the info. 
"""

class SensitiveInfo:
	def __init__(self):
		self.users = ['nick', 'tom', 'ben', 'mike']

	def read(self):
		print('There are {} users: {}'.format(len(self.users),\
		 ' '.join(self.users)))

	def add(self, user):
		self.users.append(user)
		print('Added user {}'.format(user))


class Info:
	"""
	The proxy of SensitiveInfo.
	"""

	def __init__(self):
		self.protected = SensitiveInfo()
		self.secret = 'HardToGuess'

	def read(self):
		self.protected.read()

	def add(self, user):
		sec = input('What is the secret? ')
		self.protected.add(user) if sec == self.secret \
		else print('That\'s wrong!')


def main():
	info = Info()

	while True:
		print('1. read list |==| 2. add user |==| 3.quit')
		key = input('choose option: ')
		if key == '1':
			info.read()
		elif key == '2':
			name = input('choose username: ')
			info.add(name)
		elif key == '3':
			exit()
		else:
			print('unknown option: {}'.format(key))

if __name__ == "__main__":
	main()


"""
Some application of proxy design pattern:
ZeroMQ
python lib: weakref.proxy
"""