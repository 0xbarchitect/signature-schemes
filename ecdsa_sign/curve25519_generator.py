def modular_inverse(a, p):
  """Compute the modular inverse of a modulo p using the extended Euclidean algorithm."""
  if a == 0:
      raise ValueError("Inverse does not exist")
  lm, hm = 1, 0
  low, high = a % p, p
  while low > 1:
      ratio = high // low
      nm, new = hm - lm * ratio, high - low * ratio
      lm, low, hm, high = nm, new, lm, low
  return lm % p

def compute_generator_coordinates():
  # Define the prime p for the field F_p
  p = 2**255 - 19

  # Define the curve parameter d
  d = -121665 * modular_inverse(121666, p) % p

  # Given y-coordinate of the generator point G
  y = 4 * modular_inverse(5, p) % p

  # Compute x^2 using the curve equation: x^2 = (y^2 - 1) / (d * y^2 + 1)
  y2 = y * y % p
  x2 = (y2 - 1) * modular_inverse(d * y2 + 1, p) % p

  # Compute x by taking the square root of x^2
  # In practice, you would use a library function to compute the square root in F_p
  # Here, we assume x is the positive square root
  x = pow(x2, (p + 1) // 4, p)

  return x, y

x, y = compute_generator_coordinates()
print(f"Generator point G coordinates:\nx = {x}\ny = {y}")