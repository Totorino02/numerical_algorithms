from os.path import dirname
import sys
sys.path.append(dirname(dirname(dirname(__file__))) + "/numerical_algorithms")

from interpolation.functions import moindre_carre, lagrange, newton
from interpolation.polynome import Polynomial

import matplotlib.pyplot as plt
import numpy as np



#arr = [[-2, 5], [-1, 2], [0, 1], [1, 2], [2, 5], [3, 10]]
arr = [[-3, -28], [-2, -9], [-1, -2], [0, -1], [1, 0], [2, 7], [3, 26]]
x = [a[0] for a in arr]
y = [a[1] for a in arr]


n = len(arr)
p = 3
moindre_carre_results = moindre_carre(arr, p)
lagrange_results = lagrange(arr)
newton_results = newton(arr)


""" d = Polynomial(len(arr))
d.setCoeff(lagrange_results)
print("lagrange ", d)

d = Polynomial(p+1)
d.setCoeff(moindre_carre_results)

print("moindre  ", d)
"""

plt.figure()
plt.scatter(x, y, label="poles")

xs = np.arange(-4, 4.1, 0.1)


mc = lambda x: sum(moindre_carre_results[i] * x ** i for i in range(p+1))
ys = mc(xs)
plt.plot(xs, ys, c="c", lw=2, ls="-.", label=f"moindres carres deg : {p}")


lg = lambda x: sum(lagrange_results[i] * x ** i for i in range(n))
ys = [lg(x) for x in xs]
plt.plot(xs, ys, c="r", lw=2, ls="--", label="lagrange")

nt = lambda x: sum(newton_results[i] * x ** i for i in range(n))
ys = [nt(x) for x in xs]
plt.plot(xs, ys, c="g", lw=2, ls=":", label="newton")

plt.legend()
plt.grid()
plt.show()
