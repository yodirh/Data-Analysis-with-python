#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = a**2
    b = a.sum(axis=1)
    b = np.sqrt(b)
    return np.array(b)
    #return np.sqrt(np.sum(a**2, axis=1))

def main():
    
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    print(vector_lengths(x))

if __name__ == "__main__":
    main()
