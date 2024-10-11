from py_ecc.optimized_bls12_381 import G1, G2, pairing

# Ensure the points are correctly defined
P = G1  # Generator of G1
Q = G2  # Generator of G2

# Perform the pairing operation
pairing_result = pairing(Q, P)

# Print the coordinates of P and Q
print("Coordinates of P (G1):", P)
print("Coordinates of Q (G2):", Q)

# Print the result of the pairing operation
print("Pairing result:", pairing_result)