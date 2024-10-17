import numpy as np

import matplotlib.pyplot as plt

# Define the elliptic curve equation y^2 = x^3 + 4
def elliptic_curve(x):
  return np.sqrt(x**3 + 4)

# Generate x values
x = np.linspace(-3, 3, 400)
y_positive = elliptic_curve(x)
y_negative = -elliptic_curve(x)

# Plot the elliptic curve
plt.figure(figsize=(8, 6))
plt.plot(x, y_positive, label='y = sqrt(x^3 + 4)')
plt.plot(x, y_negative, label='y = -sqrt(x^3 + 4)')
plt.title('BLS12-381: $y^2 = x^3 + 4$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()