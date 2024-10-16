def modular_inverse(a, p):
    """Compute the modular inverse of a modulo p using the extended Euclidean algorithm."""
    if a == 0:
        raise ValueError("Inverse does not exist")
    lm, hm = 1, 0
    low, high = a % p, p
    while low > 1:
        ratio = high // low
        nm, new = hm - lm * ratio, high - low * ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % p

def compute_d_parameter():
    # Define the prime p for the field F_p
    p = 2**255 - 19

    # Define the constants for the twisted Edwards curve
    numerator = -121665
    denominator = 121666

    # Compute the modular inverse of the denominator
    denominator_inv = modular_inverse(denominator, p)

    # Compute d as an integer in the finite field F_p
    d = (numerator * denominator_inv) % p

    return d

d = compute_d_parameter()
print(f"d = {d}")