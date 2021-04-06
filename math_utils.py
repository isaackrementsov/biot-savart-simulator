def add(a, b):
	return [a_i + b_i for a_i, b_i in zip(a,b)]

def subtract(a,b):
	return [a_i - b_i for a_i, b_i in zip(a,b)]

def cross(a, b):
	return [
		a[1]*b[2] - a[2]*b[1],
		a[2]*b[0] - a[0]*b[2],
		a[0]*b[1] - a[1]*b[0]
	]

def scale(c,a):
	return [c*a_i for a_i in a]

def dot(a,b):
	prod = 0

	for a_i, b_i in zip(a,b):
		prod += a_i*b_i

	return prod

def norm(a, L=2):
	val = 0

	for a_i in a:
		val += a_i**L

	return val**(1/L)
