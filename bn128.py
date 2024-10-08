import matplotlib.pyplot as plt
from py_ecc.bn128 import G1, multiply, neg, curve_order, field_modulus
import math
import numpy as np

print(f"curve order: {curve_order}")
print(f"field modulus: {field_modulus}")

xs = []
ys = []
for i in range(1,1000):
    xs.append(i)
    ys.append(int(multiply(G1, i)[1]))
    xs.append(i)
    ys.append(int(neg(multiply(G1, i))[1]))
plt.scatter(xs, ys, marker='.')

plt.show()