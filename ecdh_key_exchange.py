from py_ecc.secp256k1 import secp256k1
from secrets import randbelow

# Generate private keys for party A and B
private_key_a = randbelow(secp256k1.N)
private_key_b = randbelow(secp256k1.N)

# Generate public keys for party A and B
public_key_a = secp256k1.multiply(secp256k1.G, private_key_a)
public_key_b = secp256k1.multiply(secp256k1.G, private_key_b)

# Compute the shared secret
shared_secret_a = secp256k1.multiply(public_key_b, private_key_a)
shared_secret_b = secp256k1.multiply(public_key_a, private_key_b)

# Verify that both shared secrets are the same
assert shared_secret_a == shared_secret_b

print("Shared secret:", shared_secret_a)