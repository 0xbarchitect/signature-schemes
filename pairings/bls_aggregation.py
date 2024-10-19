from py_ecc.bls import G2ProofOfPossession as bls

# Generate private keys
private_keys = [bls.KeyGen(i.to_bytes(32, 'big')) for i in range(1, 4)]

# Generate public keys
public_keys = [bls.SkToPk(sk) for sk in private_keys]

# Messages to be signed
messages = [b"Message 1", b"Message 2", b"Message 3"]

# Sign the messages
signatures = [bls.Sign(sk, msg) for sk, msg in zip(private_keys, messages)]

# Aggregate the signatures
aggregated_signature = bls.Aggregate(signatures)

# Verify the aggregated signature
is_valid = bls.AggregateVerify(public_keys, messages, aggregated_signature)

#print(f"Aggregated signature valid: {is_valid}")