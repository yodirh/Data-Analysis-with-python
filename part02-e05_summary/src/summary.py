#!/usr/bin/env python3

import sys
import math

def summary(filename):
    List =[]
    f = open(filename, "r")
    #f = open("D:\DA Helsinki\example.txt", "r")
    for i in f:
        try:
            x = float(i)
            List.append(x)
        except ValueError:
            pass

    f.close()
    su =0.0
    j =0.0
    for i in List:
        su+= i
        
    average = su/len(List)
        

    for i in List:
        j += (i-average)**2
    sd = math.sqrt(j/(len(List)-1))
    return (su, average, sd)

def main():
    for i in sys.argv[1:]:
        l =summary(i)
        print(f"File: {i} Sum: {l[0]:.6f} Average: {l[1]:.6f} Stddev: {l[2]:.6f} ")
    
    
if __name__ == "__main__":
    main()
