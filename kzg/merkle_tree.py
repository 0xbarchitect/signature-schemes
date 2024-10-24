import hashlib

class MerkleTree:
  def __init__(self, leaves):
    self.leaves = [self._hash(leaf) for leaf in leaves]
    self.tree = self._build_tree(self.leaves)

  def _hash(self, data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

  def _build_tree(self, leaves):
    tree = [leaves]
    while len(tree[-1]) > 1:
      layer = []
      for i in range(0, len(tree[-1]), 2):
        left = tree[-1][i]
        right = tree[-1][i + 1] if i + 1 < len(tree[-1]) else left
        layer.append(self._hash(left + right))
      tree.append(layer)
    return tree

  def get_root(self):
    return self.tree[-1][0]

  def get_proof(self, index):
    proof = []
    for layer in self.tree[:-1]:
      sibling_index = index ^ 1
      if sibling_index < len(layer):
        proof.append(layer[sibling_index])
      index //= 2
    return proof

  def verify_proof(self, leaf, proof, root):
    computed_hash = self._hash(leaf)
  #   for sibling in proof:
  #     if computed_hash < sibling:
  #       computed_hash = self._hash(computed_hash + sibling)
  #     else:
  #       computed_hash = self._hash(sibling + computed_hash)
  #   return computed_hash == root

# Example usage:
leaves = ['a', 'b', 'c', 'd']
merkle_tree = MerkleTree(leaves)
root = merkle_tree.get_root()
proof = merkle_tree.get_proof(2)
is_valid = merkle_tree.verify_proof('c', proof, root)
print(f"Root: {root}")
print(f"Proof: {proof}")
print(f"Is valid: {is_valid}")