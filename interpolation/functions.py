from systems_of_algebraic_equations.matrix import Matrix
from systems_of_algebraic_equations.functions import gauss
from interpolation.polynome import Polynomial

import numpy as np


def lagrange(arr):
    n = len(arr) - 1
    xs = [a[0] for a in arr]
    ys = [a[1] for a in arr]
    p = Polynomial(n)

    for i in range(n+1):
        phi = Polynomial(0)
        phi.coeffs[0] = 1
        for j in range(n+1):
            if j != i:
                q = Polynomial(1)
                q.setCoeff([-1 * xs[j], 1])
                phi = Polynomial.mult(phi, q)
                phi = Polynomial.mult(phi, 1 / (xs[i] - xs[j]), poly=False)

        k = Polynomial.mult(phi, ys[i], poly=False)
        p = Polynomial.add(p, k)

        """ 
        phi = Polynomial(n)
        coef = 1 / np.prod([xs[i] - xs[j] for j in range(n+1) if j != i]) """
        

    return p.coeffs


def newton(arr):
    xs = [x[0] for x in arr]  # the values of x
    ys = [x[1] for x in arr]  # the values of y
    n = len(arr)

    def divided_dif(st, en):
        """ if st > en:
            return None """

        if st == en:
            res = ys[st]

            """ 
        elif en == (st + 1):
            res = (ys[en] - ys[st]) / (xs[en] - xs[st]) """
        else:
            res = (divided_dif(st+1, en) - divided_dif(st, en-1)) / (xs[en] - xs[st])
        
        return res

    # compute the newton coefficients
    def coeffs():
        a = [divided_dif(0, i) for i in range(n)]
        """ a = ys.copy()
        for i in range(1, n):
            for j in range(i, n):
                a[j] = (a[j] - a[i-1]) / (xs[j] - xs[i-1]) """
        return a

    a = coeffs()
    p = Polynomial(0)
    p.coeffs[0] = a[0]

    for i in range(1, n):
        phi = Polynomial(0)
        phi.coeffs[0] = 1  # neutral by multiplication

        for j in range(i):
            q = Polynomial(1)
            q.setCoeff([-xs[j], 1])
            phi = Polynomial.mult(phi, q)

        phi = Polynomial.mult(phi, a[i], poly=False)
        #print("sd  ", phi)
        p = Polynomial.add(p, phi)
        #print("p : ", p)

    return p.coeffs
    

def moindre_carre(arr, p=3):
    xs = [a[0] for a in arr]
    
    sums = [sum(x**k for x in xs) for k in range(2*p, -1, -1)]
    sums[-1] = len(arr) + 1

    datap = [[sums[i+j] for i in range(p+1)] for j in range(p+1)]

    P = Matrix(p, p)
    P.set_data(datap)

    datan = [[sum(a[0]**z * a[1] for a in arr)] for z in range(p, -1, -1)]

    N = Matrix(p, 1)
    N.set_data(datan)

    results = gauss(P, N)
    return results[::-1]
