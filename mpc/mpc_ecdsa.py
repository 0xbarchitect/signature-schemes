from ecdsa import SigningKey, SECP256k1
from hashlib import sha256
import random

class MPC_ECDSA:
  def __init__(self, num_parties):
    self.num_parties = num_parties
    self.private_shares = [random.randint(1, SECP256k1.order - 1) for _ in range(num_parties)]
    self.public_key = self._compute_public_key()

  def _compute_public_key(self):
    total_private_key = sum(self.private_shares) % SECP256k1.order
    signing_key = SigningKey.from_secret_exponent(total_private_key, curve=SECP256k1)
    return signing_key.verifying_key

  def sign(self, message):
    message_hash = sha256(message.encode()).digest()
    k = random.randint(1, SECP256k1.order - 1)
    R = k * SECP256k1.generator
    r = R.x() % SECP256k1.order
    s_shares = [(k - r * share) % SECP256k1.order for share in self.private_shares]
    s = sum(s_shares) % SECP256k1.order
    return (r, s)

  def verify(self, message, signature):
    r, s = signature
    message_hash = sha256(message.encode()).digest()
    w = pow(s, -1, SECP256k1.order)
    u1 = (int.from_bytes(message_hash, 'big') * w) % SECP256k1.order
    u2 = (r * w) % SECP256k1.order
    point = u1 * SECP256k1.generator + u2 * self.public_key.pubkey.point
    return point.x() % SECP256k1.order == r

# Example usage
if __name__ == "__main__":
  mpc_ecdsa = MPC_ECDSA(num_parties=3)
  message = "Hello, MPC ECDSA!"
  signature = mpc_ecdsa.sign(message)
  print("Signature:", signature)
  is_valid = mpc_ecdsa.verify(message, signature)
  print("Signature valid:", is_valid)