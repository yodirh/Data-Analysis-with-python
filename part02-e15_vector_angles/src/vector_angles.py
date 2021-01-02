#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import math

def vector_angles(X, Y):
    a = np.sqrt(np.sum(X*X, axis=1))
    b = np.sqrt(np.sum(Y*Y, axis=1))
    c = np.sum(X*Y, axis =1)

    bottom = a*b
    div= c/bottom

    d = np.arccos(np.clip(div, -1.0, 1.0))
    e= np.degrees(d)

    return e

def main():
    x = np.array([[0,0,1], [-1, 1, 0]])
    y = np.array([[0,1,0], [1,1,0]])
    print(vector_angles(x,y))

if __name__ == "__main__":
    main()
