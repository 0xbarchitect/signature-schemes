import numpy as np

import matplotlib.pyplot as plt

# Define the elliptic curve parameters
a = -1
b = 1

# Define the range for x values
x = np.linspace(-2, 2, 400)

# Calculate the corresponding y values for the elliptic curve y^2 = x^3 + ax + b
y_squared = x**3 + a*x + b

# Plot the elliptic curve
plt.figure(figsize=(8, 6))
plt.plot(x, np.sqrt(y_squared), label='y = sqrt(x^3 + ax + b)')
plt.plot(x, -np.sqrt(y_squared), label='y = -sqrt(x^3 + ax + b)')
plt.title('Elliptic Curve: y^2 = x^3 + ax + b')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
#plt.show()

# Select an arbitrary x coordinate
x_coord = 0.5

# Calculate the corresponding y coordinates for the selected x coordinate
y_coords = np.sqrt(x_coord**3 + a*x_coord + b)

# Draw a vertical line at the selected x coordinate
plt.axvline(x=x_coord, color='red', linestyle='--', label=f'x = {x_coord}')

# Mark the points where the vertical line intersects the elliptic curve
plt.scatter([x_coord, x_coord], [y_coords, -y_coords], color='red')

# Mark the point on the X axis
plt.scatter([x_coord], [0], color='blue', label=f'({x_coord}, 0)')

# Re-plot the elliptic curve to ensure it is on top
plt.legend()
plt.show()