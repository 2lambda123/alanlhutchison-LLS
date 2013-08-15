#!/usr/bin/env python

import numpy as np
import scipy
from scipy import sparse
class Foo():
    def __init__(self, f=lambda x: x):
        self.f = f
    def do(self, x):
        return self.f(x)

def thresh(w):
    return 1 if w >3 else 0

def main():
    identity = Foo()
    identity.f = thresh
    ff = np.frompyfunc(identity.f,1,1)
    
    #if you use this one you will throw an error with lil_matrix
    d = ff(np.arange(16))

    #if you use this one you will be able to use lil_matrix
    #d = np.arange(16)


    dd = scipy.sparse.lil_matrix(d)
    print dd


if __name__ == "__main__":
    main()


