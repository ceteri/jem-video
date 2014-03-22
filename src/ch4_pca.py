## @JustGlowing 2011-07-22
## http://glowingpython.blogspot.com/2011/07/principal-component-analysis-with-numpy.html

import numpy as np

def princomp (A):
    """
    principal components analysis on the N x P data matrix A
    rows correspond to observations, columns to variables
    """

    # subtract the mean (along columns)
    M = (A - np.mean(A.T, axis=1)).T

    # NB: results are not always sorted
    [latent, coeff] = np.linalg.eig(np.cov(M))

    # projection of the data in the new space
    score = np.dot(coeff.T, M)

    return coeff, score, latent


## analyze each judge's scores for our bartendrs
A = np.array([
        [ 5.1, 4.9, 4.7, 4.6, 5.7, 5.7, 6.2, 5.1, 5.7, 6.5, 7.7, 7.7, 6.0, 6.9, 5.6 ],
        [ 3.5, 3.0, 3.2, 3.1, 3.0, 2.9, 2.9, 2.5, 2.8, 3.0, 3.8, 2.6, 2.2, 3.2, 2.8 ],
        [ 1.4, 1.4, 1.3, 1.5, 4.2, 4.2, 4.3, 3.0, 4.1, 5.5, 6.7, 6.9, 5.0, 5.7, 4.9 ],
        [ 0.2, 0.2, 0.2, 0.2, 1.2, 1.3, 1.3, 1.1, 1.3, 1.8, 2.2, 2.3, 1.5, 2.3, 2.0 ],
        ])

coeff, score, latent = princomp(A.T)

print coeff
print score
print latent

portion_variance = map(lambda x: x / sum(latent), latent)
print portion_variance


## visualize the components
from numpy import mean,cov,double,cumsum,dot,linalg,array,rank
from pylab import plot,subplot,axis,stem,show,figure

figure()
subplot(121)

# every eigenvector describes the direction of a principal component
m = mean(A, axis=1)
plot([0, -coeff[0, 0] *2] + m[0], [0, -coeff[0, 1] * 2] + m[1], '--k')
plot([0, coeff[1, 0] * 2] + m[0], [0, coeff[1, 1] * 2] + m[1], '--k')
plot(A[0,:], A[1,:], 'ob') # the data
axis('equal')
subplot(122)

# plot new data
plot(score[0,:], score[1,:], '*g')
axis('equal')
show()
