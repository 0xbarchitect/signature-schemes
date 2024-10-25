from py_ecc import bn128
from py_ecc.bn128 import FQ, FQ2, FQ12, G1, G2, pairing, add, multiply, neg, is_on_curve

# kzg_aggregation.py


# Example KZG proof aggregation

def kzg_commitment(polynomial, g1):
  commitment = G1
  for i, coeff in enumerate(polynomial):
    commitment = add(commitment, multiply(g1, coeff))
  return commitment

def kzg_proof(polynomial, x, g1):
  quotient, remainder = divmod(polynomial, [x])
  assert remainder == 0, "x is not a root of the polynomial"
  return kzg_commitment(quotient, g1)

def aggregate_kzg_proofs(proofs):
  aggregated_proof = G1
  for proof in proofs:
    aggregated_proof = add(aggregated_proof, proof)
  return aggregated_proof

# Example usage
if __name__ == "__main__":
  # Example polynomial coefficients
  polynomial = [FQ(1), FQ(2), FQ(3)]  # Represents 1 + 2x + 3x^2
  # x = FQ(5)
  # g1 = bn128.G1

  # # Generate KZG commitment
  # commitment = kzg_commitment(polynomial, g1)
  # print("KZG Commitment:", commitment)

  # # Generate KZG proof
  # proof = kzg_proof(polynomial, x, g1)
  # print("KZG Proof:", proof)

  # # Aggregate multiple proofs
  # proofs = [proof, proof]  # Example with two identical proofs
  # aggregated_proof = aggregate_kzg_proofs(proofs)
  # print("Aggregated KZG Proof:", aggregated_proof)