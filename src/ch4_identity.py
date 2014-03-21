import numpy as np
A = np.array([1, 2, 3, 4]).reshape(2, 2)
I = np.array([1, 0, 0, 1]).reshape(2, 2)

print I
print np.dot(A, I)
