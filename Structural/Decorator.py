"""
Decorator Pattern.
To make addition actions to func or methods without modify origin code.
"""

from functools import wraps

def memoize(fn):
	known = dict()

	@warps(fn):
	def memoizer(*args):
		if args not in known:
			known[args] = fn(*args)
		return known[args]
	# Only apply decorator in some conditions
	cond = True
	return memoizer if cond else fn


@memoize
def nsum(n):
	"""Return sum of first n numbers"""
	assert(n >= 0), 'n cannot be less than 0'
	return 0 if n == 0 else n + nsum(n-1)

@memoize
def fibonacci(n):
	"""Return nth number in fibonacci"""
	assert(n >= 0), 'n cannot be less than 0'
	return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)

