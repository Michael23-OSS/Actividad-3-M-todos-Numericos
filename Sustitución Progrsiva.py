import numpy as np

#Declaración de variables

def solveLU(L,b):
     L = np.array(L,float)
     b = np.array(b,float)
     n,_=np.shape(L)
     y = np.zeros(n)

     #Sustitución Progresiva
     for i in range(n):
          sumj = 0
          for j in range(i):
               sumj += L[i,j] * y[j]
          y[i] = (b[i]-sumj)/L[i,i]
     return y

#Implementación de la matriz

a = np.array([[6, 0, 0, 0],
              [3, 6, 0, 0],
              [4, -2, 7, 0],
              [5, -3, 9, 21]])

b = np.array([[12],
              [-12],
              [14],
              [-2]])
print('')
print('Matriz')
print('')
print(a)
print('---------------------------------'),
print(b)
print('')
print('Sustitución Progresiva:')
print('')
print('Resultados:')
print(np.linalg.solve(a,b))
