import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the elliptic curve
a = -1
b = 1

# Define the range for x
x = np.linspace(-2, 2, 400)

# Calculate y^2 = x^3 + ax + b
y_squared = x**3 + a*x + b

# Plot the positive and negative square roots of y_squared
plt.figure(figsize=(8, 6))
plt.plot(x, np.sqrt(y_squared), label=r'$y = \sqrt{x^3 + ax + b}$', color='b')
plt.plot(x, -np.sqrt(y_squared), label=r'$y = -\sqrt{x^3 + ax + b}$', color='r')

# Add labels and title
plt.title('Elliptic Curve: $y^2 = x^3 + ax + b$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.show()