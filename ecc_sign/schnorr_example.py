import hashlib
import random

# Parameters for the Schnorr signature scheme
p = 23  # A prime number
q = 11  # A prime factor of p-1
g = 2   # A generator of the subgroup of order q in Z_p*

# Key generation
def generate_keys():
    x = random.randint(1, q-1)  # Private key
    y = pow(g, x, p)            # Public key
    return x, y

# Signing
def sign(message, x):
    k = random.randint(1, q-1)
    r = pow(g, k, p)
    e = int(hashlib.sha256((str(r) + message).encode()).hexdigest(), 16) % q
    s = (k - x * e) % q
    return r, s

# Verification
def verify(message, r, s, y):
    e = int(hashlib.sha256((str(r) + message).encode()).hexdigest(), 16) % q
    v1 = pow(g, s, p) * pow(y, e, p) % p
    return v1 == r

# Example usage
if __name__ == "__main__":
    message = "Hello, Schnorr!"
    x, y = generate_keys()
    r, s = sign(message, x)
    valid = verify(message, r, s, y)
    print(f"Message: {message}")
    print(f"Public Key: {y}")
    print(f"Signature: (r={r}, s={s})")
    print(f"Signature valid: {valid}")