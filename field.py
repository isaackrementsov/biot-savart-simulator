import math
from math_utils import cross, norm, subtract, scale

class Field:

    mu_0 = 4*math.pi * 10**(-7)
    k = 10**(-7) # mu_0/4pi

    def __init__(self, I, L):
        self.I = I
        self.L = L

    def B(self, P, scale_up=True):
        def dB(l,t,dl):
            r = subtract(P, l)
            return self.I(l)*(cross(dl, r)/norm(r)**3)

        if scale_up:
            return self.L.integrate(dB)
        else:
            return scale(k, self.L.integrate(dB))
