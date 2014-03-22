## @JustGlowing 2011-07-22
## http://glowingpython.blogspot.com/2011/07/principal-component-analysis-with-numpy.html

from numpy import mean,cov,double,cumsum,dot,linalg,array,rank
from pylab import plot,subplot,axis,stem,show,figure

def princomp (A):
    """
    principal components analysis on the N x P data matrix A
    rows correspond to observations, columns to variables
    """

    # subtract the mean (along columns)
    M = (A-mean(A.T, axis=1)).T

    # attention: not always sorted
    [latent, coeff] = linalg.eig(cov(M))

    # projection of the data in the new space
    score = dot(coeff.T, M) 

    return coeff, score, latent


## compute the eigenvalues and eigenvectors of a covariance matrix

A = array([[ 2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9 ],
           [ 2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1 ]
           ])

coeff, score, latent = princomp(A.T)

print coeff
print score
print latent

## visualize the components
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
