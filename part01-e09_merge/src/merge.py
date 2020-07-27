#!/usr/bin/env python3

def merge(L1, L2):
    l5 = L1+L2
    l4 = []
    for j in range(len(l5)):
        l4.append(min(l5))
        l5.remove(min(l5))  

    return l4

def main():
    l1 = [1,5,9,12]
    l2 = [2,6,10]

    print(merge(l1,l2))
   

if __name__ == "__main__":
    main()
