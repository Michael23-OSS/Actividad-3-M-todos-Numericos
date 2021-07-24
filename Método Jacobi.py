import numpy as np

#Implementación del sistema lineal
A = np.array([[7, 1, -1, 2],
              [1, 8, 0, -2],
              [-1, 0, 4, -1],
              [2, -2, -1, 6]])

b = [3, -5, 4, -3]

# Valores iniciales
tol = 1.1  # tolerancia
error = 100000  # valor inicial error
kmax = 100  # número máximo de iteraciones
n = len(A)  # determina tamaño de 'A'
x = np.zeros(n)  # vector x inicial de ceros de longitud 'n'
x1 = np.copy(x)  # vector auxiliar de x
k = 1  # contador inicial de iteraciones
error1 = [0]
print('')
print('Sistema Lineal')
print('')
print(A)
print('---------------------------------'),
print(b)
print('')
print('Tolerancia =', tol)
print('Número de Iteraciones =', kmax)
print('')
print('Solución por el Método de Jacobi con su error')
print('')
print('Iteraciones:')
print('')

#Implementación algoritmo Jacobi
while k < kmax and error > tol:
    print("iteración: ", k)
    for i in range(n):
        sumatoria = 0
        for j in range(n):
            if i != j:
                sumatoria += (A[i][j] * x[j])
                x[i] = (b[i] - sumatoria) / A[i][
                    i]
        print("x(", i, "): ", x[i])
    # Calculo del error
    error = np.linalg.norm(x - x1)
    error1.append(error)
    x1 = np.copy(x)

    print("  error: ", error1[k])
    print()
    k += 1
