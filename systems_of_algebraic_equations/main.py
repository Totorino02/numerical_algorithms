from matrix import Matrix
from functions import *

# sample data
arrA = [[3, 2, 3, 4], [4, 4, 3, 2], [1, 4, 4, 3], [2, 3, 1, 1]]
arrB = [[4], [8], [2], [0]]

A = Matrix(4, 4)
A.setDataByArray(arrA)
A.display()

B = Matrix(4, 2)
B.setDataByArray(arrB)
B.display()

gaussResults, finalMatrix = gauss(A, B, True)
print("GAUSS : ", *gaussResults, sep="    ")
finalMatrix.display()

gaussJordanResults, finalMatrix = gaussJordan(A, B, True)
print("GAUSS JORDAN : ", *gaussJordanResults, sep="    ")
finalMatrix.display()
