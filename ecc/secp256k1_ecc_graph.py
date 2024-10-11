import matplotlib.pyplot as plt
import numpy as np

# Define a smaller elliptic curve for visualization: y^2 = x^3 - x + 1
a = -1
b = 1

# Function to calculate y values for the elliptic curve
def elliptic_curve(x, a, b):
  return np.sqrt(x**3 + a*x + b)

# Generate x values
x_vals = np.linspace(-2, 2, 400)
y_vals = elliptic_curve(x_vals, a, b)

# Plot the elliptic curve
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='secp256k1: $y^2 = x^3 + 7$', color='blue')
plt.plot(x_vals, -y_vals, color='blue')

# Example points on this smaller curve
G = (0, 1)  # Example point
G2 = (1, 1.414)  # Another example point
G_plus_2G = (1.5, 1.936)  # Result of adding G and G2

# Plot the points
plt.scatter(*G, color='red', label='G')
plt.scatter(*G2, color='green', label='2G')
plt.scatter(*G_plus_2G, color='purple', label='G + 2G')

# Annotate the points
plt.annotate('G', G, textcoords="offset points", xytext=(-10,-10), ha='center')
plt.annotate('2G', G2, textcoords="offset points", xytext=(-10,-10), ha='center')
plt.annotate('G + 2G', G_plus_2G, textcoords="offset points", xytext=(-10,-10), ha='center')

plt.title('Secp256k1 ECC operations')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()