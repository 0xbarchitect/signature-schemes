import random
from Crypto.Util import number

class ElGamal:
    def __init__(self, key_size=256):
        self.key_size = key_size
        self.p = number.getPrime(self.key_size)
        self.g = random.randint(2, self.p - 1)
        self.x = random.randint(1, self.p - 2)
        self.h = pow(self.g, self.x, self.p)

    def encrypt(self, plaintext):
        y = random.randint(1, self.p - 2)
        c1 = pow(self.g, y, self.p)
        s = pow(self.h, y, self.p)
        c2 = (plaintext * s) % self.p
        return c1, c2

    def decrypt(self, ciphertext):
        c1, c2 = ciphertext
        s = pow(c1, self.x, self.p)
        s_inv = number.inverse(s, self.p)
        plaintext = (c2 * s_inv) % self.p
        return plaintext

# Example usage
elgamal = ElGamal()
message = 42
ciphertext = elgamal.encrypt(message)
print("Ciphertext:", ciphertext)
decrypted_message = elgamal.decrypt(ciphertext)
print("Decrypted message:", decrypted_message)