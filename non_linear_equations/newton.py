"""
* ALGORITHME DE NEWTON
* Implémenté en Python
"""

from utils import deriv


def newton(fn, x0, precision = 10e-10):
    N = 5000
    found = False
    i = 0
    x = x0

    res = "Aucun resultat"

    while not found and i < N:
        y = x
        try:
            x = y - (fn(y) / deriv(fn, y, precision))
            stopCond = abs(x - y) / abs(x) < precision
            if stopCond:
                res = x
                found = True
            i += 1

        except:
            res = "Tentative de division par zero; Veuillez svp changer les parametres du programme."
            break

    return res
