from py_ecc.optimized_bn128 import G1, G2, add, multiply, neg, pairing, is_on_curve
from hashlib import sha256
import os

def hash_to_curve(message):
    # Hash the message to a point on the elliptic curve
    h = sha256(message).digest()
    point = multiply(G1, int.from_bytes(h, 'big'))
    assert is_on_curve(point, G1)
    return point

def generate_keypair():
    # Generate a random private key
    sk = int.from_bytes(os.urandom(32), 'big')
    # Derive the public key
    pk = multiply(G1, sk)
    return sk, pk

def vrf_prove(sk, message):
    # Hash the message to a curve point
    H = hash_to_curve(message)
    # Compute the VRF output
    vrf_output = multiply(H, sk)
    # Generate the proof
    proof = multiply(G2, sk)
    return vrf_output, proof

def vrf_verify(pk, message, vrf_output, proof):
    # Hash the message to a curve point
    H = hash_to_curve(message)
    # Verify the proof using pairing
    lhs = pairing(H, proof)
    rhs = pairing(vrf_output, G2)
    return lhs == rhs

# Example usage
message = b"Hello, VRF!"
sk, pk = generate_keypair()
vrf_output, proof = vrf_prove(sk, message)
is_valid = vrf_verify(pk, message, vrf_output, proof)

print("VRF Output:", vrf_output)
print("Proof is valid:", is_valid)