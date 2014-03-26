## http://pythonhosted.org//neurolab/lib.html
import numpy as np
import neurolab as nl

# create a neural network with 3 inputs, 4 neurons
# in the hidden layer, and 1 in the output layer
net = nl.net.newff([[0, 1],[0, 1],[0, 1]], [4, 1])
input = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
target = [[0], [0], [1], [1]]

# train
net.trainf = nl.train.train_gdx
error = net.train(input, target, show=10)

# test
print "expect 0", net.sim([[0, 1, 0]])
print "expect 0", net.sim([[0, 0, 0]])
print "expect 1", net.sim([[1, 1, 0]])
print "expect 1", net.sim([[1, 0, 0]])

import pylab as pl
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()

