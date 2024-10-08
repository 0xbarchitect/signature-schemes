import matplotlib.pyplot as plt

# Define the prime for the secp256k1 curve
p = 2**256 - 2**32 - 977

# Define the secp256k1 curve equation
def is_quadratic_residue(n, p):
  """Check if n is a quadratic residue modulo p using Euler's criterion."""
  return pow(n, (p - 1) // 2, p) == 1

# Choose a small range for x to visualize
x_values = range(0, 1000)  # Adjust this range for more/less points
points = []

# Find points on the curve
for x in x_values:
  print(x)
  rhs = (x**3 + 7) % p
  if is_quadratic_residue(rhs, p):
      # Find a y such that y^2 ≡ rhs (mod p)
      y = pow(rhs, (p + 1) // 4, p)  # Use the fact that p ≡ 3 (mod 4)
      points.append((x, y))
      points.append((x, p - y))  # Both y and -y are solutions

# Extract x and y coordinates
x_coords, y_coords = zip(*points)

# Plot the points
plt.figure(figsize=(10, 6))
plt.scatter(x_coords, y_coords, s=1, color='blue')
plt.title('Elliptic Curve secp256k1 over Finite Field')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()