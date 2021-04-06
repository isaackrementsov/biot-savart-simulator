import numpy as np
import matplotlib.pyplot as plt
import math

from field import Field
from curve import Curve
from math_utils import norm

# Parametrically-defined coil
R = 3
N = 10
h = 3

ti = 0
tf = 2*math.pi*N
dt = 0.001

x = lambda t: R*np.cos(t)
y = lambda t: R*np.sin(t)
z = lambda t: h*t/(2*math.pi*N)

C = Curve(x, y, z, domain=np.arange(ti, tf, dt))
I = lambda l: 1

field = Field(I, C)

'''
Dipole antenna
h = 1
w = 2
k = 10
d = 0.1

ti = 0
tf = 1
dt = 0.01
T = np.arange(ti, tf, dt)

xa = lambda t: w*np.exp(5*(t - 1)) + d/2
xb = lambda t: -w*np.exp(5*(t - 1)) - d/2
y = lambda t: h*(1 - np.exp(-k*t))
z = lambda t: 0*t

Ca = Curve(xa, y, z, T)
Cb = Curve(xb, y, z, T)

fnorm = np.sqrt(h**2 + w**2)
I = lambda l: np.sin(math.pi*(l[0] - d)/w)

field_a = Field(I, Ca)
field_b = Field(I, Cb)
'''

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.linspace(-5,5,10), np.linspace(-5,5,10), np.linspace(-5,5,10))
B_x, B_y, B_z = field.B([x, y, z])

ax.quiver(x, y, z, B_x, B_y, B_z, length=0.1, color='blue')
ax.plot(*C.l(C.domain), color='orange')
plt.show()
