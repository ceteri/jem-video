import numpy as np

A = np.array([0, 1, -2, -3]).reshape(2, 2)

print np.linalg.eig(A)
