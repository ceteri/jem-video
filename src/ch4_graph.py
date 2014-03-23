import numpy as np

A = np.array([0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]).reshape(4, 4)

print A
print np.linalg.eig(A)
