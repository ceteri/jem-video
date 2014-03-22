import numpy as np

A = np.array([3, 9, 4, 8]).reshape(2, 2)
y = [ 5, 12 ]
invA = np.linalg.inv(A)

print invA
print np.dot(invA, y)
