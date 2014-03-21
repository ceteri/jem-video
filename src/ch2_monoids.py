#!/usr/bin/env python
# encoding: utf-8

# Francisco Mota, 2011-11-09
# http://fmota.eu/blog/monoids-in-python.html
# see also: http://arxiv.org/abs/1304.7544

class Monoid (object):
    def __init__ (self, null, lift, op):
        self.null = null
        self.lift = lift
        self.op   = op
 
    def fold (self, xs):
        if hasattr(xs, "__fold__"):
            return xs.__fold__(self)
        else:
            return reduce(self.op, (self.lift(x) for x in xs), self.null)
 
    def __call__ (self, *args):
        return self.fold(args)
 
    def star (self):
        return Monoid(self.null, self.fold, self.op)


summ   = Monoid(0,  lambda x: x,      lambda a,b: a+b)
joinm  = Monoid('', lambda x: str(x), lambda a,b: a+b)
listm  = Monoid([], lambda x: [x],    lambda a,b: a+b)
tuplem = Monoid((), lambda x: (x,),   lambda a,b: a+b)
lenm   = Monoid(0,  lambda x: 1,      lambda a,b: a+b)
prodm  = Monoid(1,  lambda x: x,      lambda a,b: a*b)


## extended to define a monoid for folding Python `dict`

def dict_op (a, b):
    for key, val in b.items():
        if not key in a:
            a[key] = val
        else:
            a[key] += val

    return a


dictm  = Monoid({}, lambda x: x,      lambda a,b: dict_op(a, b))


if __name__=='__main__':
    x1 = { "a": 2, "b": 3 }
    x2 = { "b": 2, "c": 7 }

    print x1, x2
    print dictm.fold([x1, x2])
