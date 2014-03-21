## use NumPy to calculate matrix operations

import numpy as np

A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([5, 6, 7, 8]).reshape(2, 2)
x = [2, 3]

print A
print B

print np.add(A, B)
print np.dot(A, x)
