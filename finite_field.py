import libnum
import matplotlib.pyplot as plt

def generate_points(mod):
    xs = []
    ys = []
    def y_squared(x):
        return (x**3 + 3) % mod

    for x in range(0, mod):
        if libnum.has_sqrtmod_prime_power(y_squared(x), mod, 1):
            square_roots = libnum.sqrtmod_prime_power(y_squared(x), mod, 1)

            # we might have two solutions
            for sr in square_roots:
                print(f"found square root mod {mod} for x={x}: {sr}")
                ys.append(sr)
                xs.append(x)
    return xs, ys


xs, ys = generate_points(11)
fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('y^2 = x^3 + 3 (mod p)')
fig.set_size_inches(6, 6)
ax1.set_xticks(range(0,11))
ax1.set_yticks(range(0,11))
plt.grid()
plt.scatter(xs, ys)
plt.plot()

plt.show()