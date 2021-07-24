import numpy as np

#Ingresar una Matriz desde pantalla
print("")
print("Datos de la Matriz")
print("")
filas = int(input("Introduce numero de filas : "))
columnas = int(input("Introduce numero de columnas : "))
print("")

a = []
for i in range(filas):
    a.append([])
    for j in range(columnas):
        valor = float(input("fila {}, columna{} : ".format(i+1, j+1)))
        a[i].append(valor)
print("")
print("Matriz:")
print()
for filas in a:
    print("[",  end=" ")

    for elemento in filas:
        print("{:8.2f}".format(elemento), end=" ")
    print("]")

#Preestablecer una Matriz

#a = np.array([[8, 6, 9, 5],
              #[4, 5, 7, 6],
              #[2, 7, 3, 4],
              #[8, 2, 1, 0]])

#print("Matriz:")
#print("")
#print(a)

#Generar automaticamente una matriz con valores de 1 al 100

#a = np.arange(1, 26).reshape((5, 5))
#print("Matriz:")
#print("")
#print(a)


print("")
print("Norma de Frobenius:")
print(np.linalg.norm(a, 'fro'))
print("")
print("Número de condición:")
print(np.linalg.cond(a, 'fro'))
print("")