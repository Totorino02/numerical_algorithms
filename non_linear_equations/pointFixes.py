"""
* METHODE DES POINTS FIXES
* implemente en Python
"""


def fixed_points(fn, x0, precision=10e-10):
    N = 5000
    found = False
    i = 0
    res = "Aucun resultat"

    while not found and i < N:
        x1 = fn(x0)
        x2 = fn(x1)

        try:
            xe = x0 - ((x1 - x0)**2) / (x2 - 2 * x1 + x0)
            stopCond = abs(xe-x0) / abs(xe) < precision
            if stopCond:
                res = xe
                # print("POINT FIXE : ", xe)
                found = True
            else:
                x0 = xe
            i += 1

        except:
            res = "Tentative de division par zero; Veuillez svp changer les parametres du programme."
            break

    return res
        