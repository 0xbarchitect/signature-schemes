import hashlib
from typing import List, Tuple

class Polynomial:
  def __init__(self, coefficients: List[int]):
    self.coefficients = coefficients

  def evaluate(self, x: int) -> int:
    result = 0
    power = 1
    for coeff in self.coefficients:
      result += coeff * power
      power *= x
    return result

class KZGCommitmentScheme:
  def __init__(self, secret: int, degree: int):
    self.secret = secret
    self.degree = degree
    self.setup()

  def setup(self):
    self.g = [pow(self.secret, i) for i in range(self.degree + 1)]

  def commit(self, polynomial: Polynomial) -> int:
    commitment = 1
    for coeff, g_i in zip(polynomial.coefficients, self.g):
      commitment *= pow(g_i, coeff)
    return commitment

  def open(self, polynomial: Polynomial, x: int) -> Tuple[int, int]:
    y = polynomial.evaluate(x)
    quotient = Polynomial([coeff // x for coeff in polynomial.coefficients])
    proof = self.commit(quotient)
    return y, proof

  def verify(self, commitment: int, x: int, y: int, proof: int) -> bool:
    lhs = pow(self.g[0], y)
    rhs = commitment * pow(proof, x)
    return lhs == rhs

# Example usage
if __name__ == "__main__":
  secret = 123456789
  degree = 3
  polynomial = Polynomial([1, 2, 3, 4])
  kzg = KZGCommitmentScheme(secret, degree)

  commitment = kzg.commit(polynomial)
  x = 5
  y, proof = kzg.open(polynomial, x)
  is_valid = kzg.verify(commitment, x, y, proof)

  # print(f"Commitment: {commitment}")
  # print(f"Evaluation at x={x}: {y}")
  # print(f"Proof: {proof}")
  # print(f"Verification: {'valid' if is_valid else 'invalid'}")