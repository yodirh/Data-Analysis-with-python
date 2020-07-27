#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = (b**2)-(4*a*c)
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    return (x1,x2)


def main():
    print (solve_quadratic(2.507650,8.267600,5.025710))

if __name__ == "__main__":
    main()
