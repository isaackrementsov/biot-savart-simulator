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
            return self.I(l)*cross(dl, r)/norm(r)**3

        if scale_up:
            return self.L.integrate(dB)
        else:
            return scale(k, self.L.integrate(dB))


    def B_meshgrid(self, x, y, z):
        B_x = x
        B_y = y
        B_z = z

        for i in range(len(x)):
            for j in range(len(x[i])):
                for k in range(len(x[i][j])):
                    b = self.B([x[i][j][k], y[i][j][k], z[i][j][k]])
                    B_x[i][j][k] = b[0]
                    B_y[i][j][k] = b[1]
                    B_z[i][j][k] = b[2]
        print(B_x)
        return B_x, B_y, B_z

    def B_plane(self, x, z):
        B_x = x
        B_z = x

        for i in range(len(x)):
            for j in range(len(x[i])):
                b = self.B([x[i][j], 0, z[i][j]])
                B_x[i][j] = b[0]
                B_z[i][j] = b[2]

        return B_x, B_z
