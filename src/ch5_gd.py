## based on an analytic solution, we expect that the local minimum of
## the polynomial function f(x) occurs at x = 9/4 = 2.25
 
def f (x):
    return x**4 - 3 * x**3 + 2

def f_prime (x):
    """first derivative of f(x)"""
    return 4 * x**3 - 9 * x**2

def g (x):
    return x**2

def g_prime (x):
    """first dervative of g(x)"""
    return 2 * x


## inputs: f, starting value x1, termination tolerances

def gradient_descent (x1, toler, step_size, max_iter, func, func_deriv):
    x0 = 0
    print "\t".join([ "i", "x1", "error", "func(x1)" ])

    for i in xrange(max_iter):
        error = abs(x1 - x0)
        print "\t".join([ "%d %0.4e %0.4e %3.4e" % (i, x1, error, func(x1)) ])

        if abs(x1 - x0) <= toler:
            return "local minimum:", x1

        x0 = x1
        x1 = x0 - step_size * func_deriv(x0)

    return "halted"


## NB: step size is set here, and is not adaptive

x1 = 6
toler = 0.00001
step_size = 0.01
max_iter = 93

print gradient_descent(x1, toler, step_size, max_iter, f, f_prime)
