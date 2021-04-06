# Biot-Savart Calculator
![picture](https://github.com/isaackrementsov/biot-savart-simulator/blob/master/field.png?raw=true)<br/>
Calculates the magnetic field for 3d current distributions using the Law of Biot-Savart:
<br/>![equation](https://latex.codecogs.com/svg.latex?\vec%20B(\vec%20x)%20=%20\frac{\mu_0}{4\pi}\int\limits_L%20\frac{d\vec%20y\times(\vec%20x%20-%20\vec%20y)}{||\vec%20x%20-%20\vec%20y||^3})<br/>
For many simple distributions (such as coils and solenoids), the line integral in this expression is unsolvable with elementary functions for certain points.
Thus, this program provides a useful visualization and solution for any position relative to the object.
Currently only works for curves, but surfaces & regions may be added later.
