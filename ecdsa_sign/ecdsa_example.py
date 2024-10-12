from ecdsa import SigningKey, NIST384p

# Generate a new private key
private_key = SigningKey.generate(curve=NIST384p)

# Get the corresponding public key
public_key = private_key.get_verifying_key()

# Message to be signed
message = b"Hello, ECDSA!"

# Sign the message
signature = private_key.sign(message)

# Verify the signature
is_valid = public_key.verify(signature, message)

print(f"Message: {message}")
print(f"Signature: {signature.hex()}")
print(f"Signature valid: {is_valid}")