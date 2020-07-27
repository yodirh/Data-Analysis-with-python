#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    plt.subplot(1,2,1)
    plt.plot(a[:,0],a[:,1])
    plt.subplot(1,2,2)
    plt.scatter(a[:,0],a[:,1],s = (a[:,3]),c=(a[:,2]))
    plt.show()    

def main():
    a = np.array([[5,4,1,2],[4,2,1,2]])
    subfigures(a)
     

if __name__ == "__main__":
    main()
