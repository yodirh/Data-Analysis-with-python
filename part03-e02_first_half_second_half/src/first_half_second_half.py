#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    i,d = a.shape
    j = int(d/2)
    c = np.sum(a[:,:j],axis = 1)>np.sum(a[:,j:],axis=1)
    return np.array(a[c])

def main():
    a = np.array([[1, 3, 4, 2],
                [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
