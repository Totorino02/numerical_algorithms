"""
* METHODE DE LA SÉCANTE
* implemente en Python
"""


def secante(fn, a, b, precision=10e-10):
    N = 5000
    found = False
    i = 0

    # xn-1 = x0
    # xn = x1
    # xn+1 = x

    if fn(a) == 0:
        res = a
        found = True
    elif fn(b) == 0:
        res = b
        found = True

    else:
        x0 = a
        x1 = b

        while not found and i < N:
            try :
                x = x1 - (fn(x1) * (x1 - x0)) / (fn(x1) - fn(x0))
                stopCond = abs(x - x1) / abs(x) < precision
                if stopCond:
                    found = True
                    res = x
                    #print("CORDE : ", x)
                x0 = x1
                x1 = x

            except:
                res = "Tentative de division par zero; Veuillez svp changer les parametres du programme."
                break
        if i == 5000:
            res = "Nombre maximal d iterations atteint"

    return res
