#!/usr/bin/env python3

def positive_list(L):
    l =  list(filter(tes,L))

    return l
    

def tes(x):
    return x>0

def main():
    print(positive_list([2,-2,0,1,-7]))

if __name__ == "__main__":
    main()
