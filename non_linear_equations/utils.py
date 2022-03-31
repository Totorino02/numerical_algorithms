
from math import *  # used for getFunction function

def getFunction(message = "Entrez la function : f(x) = "):
    fn = input(message)
    try:
        f = eval(f"lambda x : {fn}")
        return f
    except:
        print("La funcion entree n est pas valide")
        # exit()


def deriv(fn, a, precision=0.00000001):
    result = (fn(a + precision) - fn(a)) / precision
    return result
    

def balayage(fn, a, b, pas=0.0001):
    solutions = []

    i = a
    while i < b:
        an = i
        bn = i + pas

        if fn(an) == 0:
            solutions.append([round(an, 4), round(an, 4)])
        elif fn(bn) == 0:
            solutions.append([round(bn, 4), round(bn, 4)])
        elif fn(an) * fn(bn) < 0 and abs(fn(an) - fn(bn)) < 10:
            # second condition to check fn continuity between an and bn
            # not a mathematical proof 😅
            solutions.append([round(an, 4), round(bn, 4)])
        
        i = bn

    return solutions


def is_number(st):
    try:
        float(st)
        return True
    except ValueError:
        return False