"""
* METHODE DE LA BISSECTION
* implemente en Python
"""

def bissection(fn, a, b, precision=10e-10):
    N = 5000
    found = False
    i = 0

    if fn(a) == 0:
        res = a
        found = True
    elif fn(b) == 0:
        res = b
        found = True

    else:
        while not found and i < N:
            x = (a + b) / 2

            try:
                if ((abs(b - a)) / (2 * abs(x)) < precision):
                    found = True
                    res = x

            except:
                res = "Tentative de division par zero; Veuillez svp changer les parametres du programme."
                break

            if fn(a) == 0:
                found = True
                res = a
            if fn(b) == 0:
                found = True
                res = b

            if (fn(a) * fn(x) < 0):
                b = x
            else:
                a = x

            i += 1

        if i == 5000:
            res = "Nombre maximal d iterations atteint"
   
    return res
