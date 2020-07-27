#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    c = a[:,1]>a[:,-2]
    return np.array(a[c])
    
def main():
    x =  np.array([[1, 7, 5, 6,7],
        [1,2,4,4,6]])
    print(column_comparison(x))

if __name__ == "__main__":
    main()
