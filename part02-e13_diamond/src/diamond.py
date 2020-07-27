#!/usr/bin/env python3

import numpy as np

def diamond(n):
    i = np.eye(n, dtype=int)
    m= i[:,1:]
    j = np.concatenate((i[::-1],m), axis=1)
    k= j[::-1]
    l=np.concatenate((j,k[1:,]))

    return l

def main():
    print(diamond(4))

if __name__ == "__main__":
    main()
