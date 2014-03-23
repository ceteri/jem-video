from glpk import LPX

# set up to maximize the objective function
lp = LPX()
lp.name = 'example'
lp.obj.maximize = True

# append 3 rows, named p, q, r
row_names = ["p", "q", "r"]
lp.rows.add(len(row_names))

for r in lp.rows:
    r.name = row_names[r.index]

lp.rows[0].bounds = None, 100.0
lp.rows[1].bounds = None, 600.0
lp.rows[2].bounds = None, 150.0

# append 3 cols, named x0, x1, x2
lp.cols.add(3)

for c in lp.cols:
    c.name = 'x%d' % c.index
    c.bounds = 0.0, None

# set the objective coefficients and
# non-zero entries of the constraint matrix
lp.obj[:] = [ 5.0, 3.0, 2.0 ]
lp.matrix = [ 1.0, 1.0, 3.0, 10.0, 4.0, 5.0, 1.0, 1.0, 3.0 ]

# report the objective function value and structural variables
lp.simplex(msg_lev=LPX.MSG_ALL)
print 'Z = %g;' % lp.obj.value,
print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
