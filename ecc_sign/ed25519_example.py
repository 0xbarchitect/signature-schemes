from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization

# Generate a new private key
private_key = Ed25519PrivateKey.generate()

# Sign a message
message = b"Message for Ed25519 signing"
signature = private_key.sign(message)

print(f"Message: {message}")
print(f"Signature: {signature.hex()}")

# Serialize the private key to bytes
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Load the private key from bytes
loaded_private_key = Ed25519PrivateKey.from_private_bytes(private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
))

# Get the public key from the private key
public_key = private_key.public_key()

# Verify the signature
try:
    public_key.verify(signature, message)
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid:", e)