import numpy as np
import matplotlib.pyplot as plt
from py_ecc.optimized_bls12_381 import G1, multiply

def generate_points(num_points=1000):
  points = []
  for i in range(num_points):
      point = multiply(G1, i)
      x, y = point[0], point[1]
      points.append((int(x), int(y)))
  return points

# Generate points
points = generate_points()

# Separate x and y coordinates
x_coords, y_coords = zip(*points)

# Create the plot
plt.figure(figsize=(12, 10))
plt.scatter(x_coords, y_coords, s=1, alpha=0.5)

plt.title("BLS12-381 Curve Points (G1)")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

# Save the plot
plt.savefig('bls12_381_points.png', dpi=300)
plt.show()

# Created/Modified files during execution:
#print("bls12_381_points.png")