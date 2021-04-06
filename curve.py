''''
Parametrically-defined curve in cartesian coordinates
'''

from math_utils import add, subtract

class Curve:

	def __init__(self, x, y, z, domain):
		self.x = x
		self.y = y
		self.z = z
		self.domain = domain

	def l(self, t):
		return [self.x(t), self.y(t), self.z(t)]

	# Integrate a function of (x,y,z) over the curve
	def integrate(self, integrand, scalar=False):
		S = [0,0,0]
		if scalar:
			S = 0

		lp = self.l(self.domain[0])

		for t in self.domain:
			l = self.l(t)
			dl = subtract(l, lp)

			if not scalar:
				S = add(S, integrand(l, t, dl))
			else:
				S += integrand(l, t, dl)

			lp = l

		return S
