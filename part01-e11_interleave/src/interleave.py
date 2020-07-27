#!/usr/bin/env python3

def interleave(*lists):
    b=[]
    for i in zip(*lists):  
        b.extend(i)
    return b

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
