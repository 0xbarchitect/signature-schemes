from sympy import mod_inverse

# Define the secp256k1 parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7

# Generator point G
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

def point_addition(x1, y1, x2, y2, p):
  if x1 == x2 and y1 == y2:
      # Point doubling
      lam = (3 * x1 * x1) * mod_inverse(2 * y1, p) % p
  else:
      # Point addition
      lam = (y2 - y1) * mod_inverse(x2 - x1, p) % p

  x3 = (lam * lam - x1 - x2) % p
  y3 = (lam * (x1 - x3) - y1) % p
  return x3, y3

def is_on_curve(x, y, a, b, p):
  return (y * y - (x * x * x + a * x + b)) % p == 0

# Calculate 2G (point doubling)
x2G, y2G = point_addition(Gx, Gy, Gx, Gy, p)

# Calculate G + 2G (point addition)
x3, y3 = point_addition(Gx, Gy, x2G, y2G, p)

# Verify the result is on the curve
print(f"G: ({Gx}, {Gy})")
print(f"2G: ({x2G}, {y2G})")
print(f"G + 2G: ({x3}, {y3})")
print(f"Is (G + 2G) on the curve? {is_on_curve(x3, y3, a, b, p)}")