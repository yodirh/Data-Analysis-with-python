#!/usr/bin/env python3

def transform(s1, s2):
    li = []
    
    k = list(map(int,s1.split()))
    s = list(map(int,s2.split()))

    li.extend( a*b for a,b in list(zip(k,s)))
            
    return li


def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
