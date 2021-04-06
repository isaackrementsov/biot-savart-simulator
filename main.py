import numpy as np
import matplotlib.pyplot as plt
import math

from field import Field
from curve import Curve

R = 3
N = 10
h = 3
# Parametrically defined solenoid
L = Curve(
	x=lambda t: R*np.cos(t),
	y=lambda t: R*np.sin(t),
	z=lambda t: h*t/(2*math.pi*N),
	domain=np.arange(0, 2*math.pi*N, 0.01)
)
I = lambda l: 1

field = Field(I, L)

fig = plt.figure()
ax = fig.gca(projection='3d')

x,y,z = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10), np.linspace(-5,5,10))
B_x, B_y, B_z = field.B([x, y, z])

ax.quiver(x, y, z, B_x, B_y, B_z, length=0.1, color='blue')
ax.plot(*L.l(L.domain), color='orange')
plt.show()
