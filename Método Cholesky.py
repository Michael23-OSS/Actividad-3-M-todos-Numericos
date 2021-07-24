import numpy
import scipy.linalg
from pprint import pprint

A = numpy.array([[4, 6, 10],
                 [6, 3, 19],
                 [10, 19, 62]])

L = scipy.linalg.cholesky(A, lower=True)
Lt = scipy.linalg.cholesky(A, lower=False)

print('')
print('Matriz')
print('')
pprint(A)
print('')
print('Método Cholesky')
print('')
print("Matriz L:")
pprint(L)
print('')
print("Matriz Lt:")
pprint(Lt)

