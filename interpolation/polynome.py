
class Polynomial:
    def __init__(self, degree) -> None:
        self.degree = degree
        self.coeffs = [0] * (self.degree + 1)

    def setCoeff(self, arr=None) -> None:
        n = self.degree
        if arr:
            self.coeffs = arr.copy()
            self.degree = len(arr) - 1
            """ for i in range(n):
                self.coeffs[i] = arr[i] """
        else :
            for i in range(n):
                k = int(input(f"Enter coefficient {i} : "))
                self.coeffs[i] = k

    def __repr__(self) -> str:
        n = self.degree + 1
        st = "f(x) = "
        #for k in range(n, -1, -1):
        for k in range(n):
            coef = self.coeffs[k]
            """ if k == n:
                if coef > 0:
                    st += str(coef) + "X^" + str(k) 
                elif coef < 0:
                    st += " - " + str(abs(coef)) + "X^" + str(k) """
            if k == 1:
                if coef < 0:
                    st += " - " + str(abs(coef)) + "X"
                elif coef > 0:
                    st += " + " + str(coef) + "X" if coef != 1 else " + " + "X"
            elif k == 0:
                if coef < 0:
                    st += " - " + str(abs(coef))
                elif coef > 0:
                    st += str(coef)
            else:
                if coef < 0:
                    st += " - " + str(abs(coef)) + "X^" + str(k)
                elif coef > 0:
                    st += " + " + str(coef) + "X^" + str(k) if coef != 1 else " + " + "X^" + str(k)

        return st

    def add(p1, p2):
        n = p1.degree + 1
        m = p2.degree + 1
        if n > m:
            p = Polynomial(n)
            for k in range(m):
                p.coeffs[k] = p1.coeffs[k] + p2.coeffs[k]
            for k in range(m, n):
                p.coeffs[k] = p1.coeffs[k]
        
        else:
            p = Polynomial(m)
            for k in range(n):
                p.coeffs[k] = p1.coeffs[k] + p2.coeffs[k]
            for k in range(n, m):
                p.coeffs[k] = p2.coeffs[k]

        return p
    
    def mult(p1, p2, poly=True):
        if not poly:
            m = p1.degree
            p = Polynomial(m)
            p.coeffs = [x * p2 for x in p1.coeffs]
        else:
            m = p1.degree + p2.degree
            p = Polynomial(m)
            p.coeffs = [0] * (m + 1)

            for i in range(p1.degree + 1):
                for j in range(p2.degree + 1):
                    p.coeffs[i+j] += p1.coeffs[i] * p2.coeffs[j]

        return p
