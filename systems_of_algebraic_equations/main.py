from os import sep
from matrix import Matrix
from functions import *

# sample data
arrA = [[3, 2, 3, 4], [4, 4, 3, 2], [1, 4, 4, 3], [4, 5, 6, 7]]
arrB = [[4], [8], [2], [7]]

""" 
arrA = [[1, -1, 2, -1], [2, -2, 3, -3], [1, 1, 1, 0], [1, -1, 4, 3]]
arrB = [[-8], [-20], [-2], [4]]

arrA = [[1, 1, 4], [0, 2, 1], [1, 3, 2]]
arrB = [[2], [3], [1]]

arrA = [[1, 0, 1], [-1, 1, 2], [1, -1, 1]]
arrB = [[2], [2], [1]]
 
arrA = [[3, -1, 2], [1, 2, 3], [2, -2, -1]]
arrB = [[12], [11], [2]]

arrA = [[0, 2, 1], [1, 0, 0], [3, 0, 1]]
arrB = [[5], [-1], [-2]]
"""

arrA = [[34, 0, 10], [0, 10, 0], [10, 0, 6]]
arrB = [[44], [0], [15]]

A = Matrix(3, 3)
A.set_data(arrA)
A.display()

B = Matrix(3, 1)
B.set_data(arrB)
B.display()


 
""" arrA = [[1, 2], [3, 4]]
arrB = [[3], [7]] """
""" 
A = Matrix(3, 3)
A.set_data(arrA)
A.display()

B = A.triangularize()
c = A.triangularize(False)
d = B.multiply(c)

B.display()
c.display()
d.display()

 """
""" B = Matrix(4, 1)
B.set_data(arrB)
B.display() """

gauss_results, final_matrix = gauss(A, B, return_final_matrix=True)
print("GAUSS : ", *gauss_results, sep="    ")
#final_matrix.display()

gauss_jordan_results, final_matrix = gauss_jordan(A, B, return_final_matrix=True)
print("GAUSS JORDAN : ", *gauss_jordan_results, sep="    ")
#final_matrix.display()

lu_results, l, u, C = LU_Crout(A, B, return_final_matrixes=True)
print("LU Crout : ", *lu_results, sep="    ")
""" l.display()
u.display()
C.display() """

jacobi_results = jacobi(A, B)
print("JACOBI : ", *jacobi_results, sep="    ")

gauss_seidel_results = gauss_seidel(A, B)
print("GAUSS SEIDEL : ", *gauss_seidel_results, sep="    ")
