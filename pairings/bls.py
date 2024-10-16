from py_ecc.bls.g2_primitives import G2ProofOfPossession as bls
from py_ecc.optimized_bls12_381 import curve_order
from py_ecc.optimized_bls12_381 import G2, G1, pairing, FQ12
from hashlib import sha256

private_key = int.from_bytes(sha256(b"some random seed").digest(), 'big') % curve_order

# Generate the corresponding public key
public_key = bls.SkToPk(private_key)

# Message to be signed
message = b"Hello, BLS!"

# Sign the message
signature = bls.Sign(private_key, message)

# Verify the signature
is_valid = bls.Verify(public_key, message, signature)

print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print(f"Message: {message}")
print(f"Signature: {signature}")
print(f"Signature valid: {is_valid}")
