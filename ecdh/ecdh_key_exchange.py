from py_ecc.secp256k1 import secp256k1
from secrets import randbelow
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

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

# Generate an arbitrary message
message = b"This is a secret message."

# Derive a 256-bit AES key from the shared secret using SHA-256
shared_secret_bytes = shared_secret_a[0].to_bytes(32, byteorder='big') + shared_secret_a[1].to_bytes(32, byteorder='big')
aes_key = hashlib.sha256(shared_secret_bytes).digest()

# Encrypt the message using AES
cipher = AES.new(aes_key, AES.MODE_CBC)
iv = cipher.iv
ciphertext = cipher.encrypt(pad(message, AES.block_size))

print("Ciphertext:", ciphertext)
print("IV:", iv)

# Decrypt the message to verify
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", decrypted_message)