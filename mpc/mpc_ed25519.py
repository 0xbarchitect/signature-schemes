import os

import nacl.signing
import nacl.encoding

class MPCWallet:
    def __init__(self):
        self.signing_keys = []
        self.verifying_keys = []

    def generate_keys(self, num_parties):
        for _ in range(num_parties):
            signing_key = nacl.signing.SigningKey.generate()
            verifying_key = signing_key.verify_key
            self.signing_keys.append(signing_key)
            self.verifying_keys.append(verifying_key)

    def sign_message(self, message):
        signatures = []
        for signing_key in self.signing_keys:
            signed_message = signing_key.sign(message.encode('utf-8'))
            signatures.append(signed_message.signature)
        return signatures

    def verify_signatures(self, message, signatures):
        for verifying_key, signature in zip(self.verifying_keys, signatures):
            try:
                verifying_key.verify(message.encode('utf-8'), signature)
            except nacl.exceptions.BadSignatureError:
                return False
        return True

if __name__ == "__main__":
    wallet = MPCWallet()
    num_parties = 3
    wallet.generate_keys(num_parties)

    message = "This is a test message."
    signatures = wallet.sign_message(message)

    is_valid = wallet.verify_signatures(message, signatures)
    print(f"Signatures valid: {is_valid}")