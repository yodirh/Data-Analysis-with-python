#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    result = [i for i in a]

    return result

def get_columns(a):
    List = []
    j = a.T
    m,p = j.shape

    for i in range(0,m):
        List.append(j[i])
    return List

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
