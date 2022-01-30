print('---------------"Matrices/diagonal matrices"-------------------')
from numpy import*
arr = array([
    [1,2,3],
    [4,5,6]
])
m = matrix(arr)
print(m)
print(m.size)
A = matrix('1 2 3; 4 5 6; 7 8 9')
print(diagonal(A))
B = matrix('1 2 3; 4 5 6 ; 7 8 9')
C = A+B
print("Sum of two matrices",C)
D = A*B
print("Multiplication of two matrices",D)