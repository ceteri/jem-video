## use NumPy to calculate vector operations

import numpy as np

a = 3
b = 2
x = np.array([ 2, 3, 1, 0 ])
y = np.array([ 5, 1, 5, 0 ])

print np.add(x, a)

print np.dot(b, x)

print np.add(x, y)

print np.dot(x, y)
