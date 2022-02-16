import copy 
from matrix import Matrix


def solveTiangularMatrix(A, B=None, method="lift", A_is_extended=False, return_list=True):
    """ if not (A.is_upper_triangular_matrix and B.is_col_matrix):
        print("first matrix should be upper triangle, second one should be a column matrix")
        exit() """
    # TODO verify if A is a triangular matrix and B is a column matrix

    n = A.row   
    results = [None] * n

    if method == "lift":
        if A_is_extended:
            a = A.data[n-1][-1]
            b = A.data[n-1][n-1]
            c = lambda i : A.data[i][-1]

        else:
            a = B.data[n-1][0]
            b = A.data[n-1][n-1]
            c = lambda i : B.data[i][0]

        # calcul of the last solution wich will be used to calculate the other ones
        xn = round((a / b), 4)
        results[-1] = xn

        # calcul of the other solutions recursively
        for i in range(n-2, -1, -1):
            _sum = sum([A.data[i][j] * results[j] for j in range(i+1, n)])
            results[i] = round((c(i) - _sum ) / A.data[i][i], 4)
    
    elif method == "descent":
        if A_is_extended:
            a = A.data[0][-1]
            b = lambda i : A.data[i][-1]

        else:
            a = B.data[0][0]
            b = lambda i : B.data[i][0]

        results[0] = a / A.data[0][0]
        for i in range(1, n):
            results[i] = (b(i) - sum([A.data[i][k] * results[k] for k in range(i)])) / A.data[i][i]

    else:
        print("Invalid method ....")

    if return_list:
        return results
    else :
        res = Matrix(n, 1)
        res.set_data([[results[i]] for i in range(n)])
        return res


def gauss(A, B, return_final_matrix=False):

    if not (A.is_squared and B.is_col_matrix) :
        print("first matrix should be squared, second one should be a column matrix")
        exit()

    # w = working matrix, obtained by appending B to A
    w = A.extend(B)

    # upper triangularization of w
    w = w.triangularize()

    results = solveTiangularMatrix(w, A_is_extended=True)

    if return_final_matrix:
        return results, w
    else:
        return results


def gauss_jordan(A, B, return_final_matrix=False):
    if not (A.is_squared and B.is_col_matrix) :
        print("first matrix should be squared, second one should be a column matrix")
        exit()

    # w = working matrix, obtained by appending B to A
    w = A.extend(B)

    # diagonalization of w
    w = w.diagonalize()

    # divide each element of row k by w.data[k][k] 
    n = w.row
    for i in range(n):
        w.data[i][-1] /= w.data[i][i]

    # retrieving results
    results = [round(w.data[i][-1], 4) for i in range(n)]

    if return_final_matrix:
        return results, w
    else:
        return results


def LU_Crout(A, B, return_final_matrixes=False):

    # work on a copy so that we do not modify the original matrix
    W = copy.deepcopy(A)

    def changePivotRow(i):
        arr = [0] * n
        if i == 0:
            matrix = W
        else:
            matrix = l
        for z in range(i, n):
            arr[z] = abs(matrix.data[z][i])
        m = arr.index(max(arr))

        l.data[i], l.data[m] = l.data[m], l.data[i]
        W.data[i], W.data[m] = W.data[m], W.data[i]
        o[i], o[m] = o[m], o[i]


    if not W.is_squared:
        print("Matrix should be squared")
        return
    n = W.row

    l = Matrix(n, n, 0)
    u = Matrix(n, n, 0)
    for k in range(n):
        u.data[k][k] = 1
        
    # vector to keep track of line inversions
    o = [i for i in range(n)]

    # if pivot is null, invert pivot row with the row with the largest abs of first term 🌀
    if l.data[0][0] == 0:
        changePivotRow(0)
    
    #first column of L is the same as first column of A
    for i in range(n):
        l.data[i][0] = W.data[i][0]
       
    #first line of U
    for i in range(1, n):
        u.data[0][i] = W.data[0][i] / l.data[0][0]

    for i in range(1, n-1):
        # clacul of pivot
        l.data[i][i] = W.data[i][i] - sum([l.data[i][k] * u.data[k][i] for k in range(i)])

        for j in range(i+1, n):
            # calcul of col i of L
            l.data[j][i] = W.data[j][i] - sum([l.data[j][k] * u.data[k][i] for k in range(j)])


        # if pivot is null, invert pivot row with the row with the largest abs of first term 🌀
        if l.data[i][i] == 0:
            changePivotRow(i)
            
        for j in range(i+1, n):
            # calcul of line i of U
            u.data[i][j] = (W.data[i][j] - sum([l.data[i][k] * u.data[k][j] for k in range(i)])) / l.data[i][i]


    # calcul of l.data[n-1][n-1]
    l.data[n-1][n-1] = W.data[n-1][n-1] - sum([l.data[n-1][k] * u.data[k][n-1] for k in range(n-1)])

    # update B with o values
    C = copy.deepcopy(B)
    for y in range(n):
        C.data[y][0] = B.data[o[y]][0]

    y = solveTiangularMatrix(l, C, "descent", return_list=False)
    x = solveTiangularMatrix(u, y, "lift")


    if return_final_matrixes:
        return x, l, u, C
    else:
        return x
    