import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

#Implementación de la matriz
A = np.array([[6, 0, 0, 0],
              [3, 6, 0, 0],
              [4, -2, 7, 0],
              [5, -3, 9, 21]])

b = np.array([[12],
              [-12],
              [14],
              [-2]])

#  Factorización matricial,
#  la matriz de permutación P es la identidad,
#  Obtenemos la matriz L y con la permutación la U,
#  Por ultimo obtenemos los resultados de x

P, L, U = lu(A)
np.allclose(L @ U, A)
LU, p = lu_factor(A)
x1 = lu_solve((LU, p), b)
np.allclose(x1, np.linalg.solve(A, b))

print('')
print('Matriz')
print('')
print(A)
print('---------------------------------'),
print(b)
print('')
print('Descomposición LU')
print('')
print('La matriz L es:')
print(L)
print('')
print('La matriz U es:')
print(U)
print('')
print('Resultados:')
print(x1)