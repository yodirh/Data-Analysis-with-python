#!/usr/bin/env python3

import sys

def file_count(filename = ""):
    f = open(filename, "r")
    #f = open ("D:\DA Helsinki\est.txt", "r")
    line = 0
    words = 0
    chars = 0
    for i in f:
        line +=1
        j = i.split()
        words += len(j)
        chars += len(i)
    f.close()
            
    return (line, words, chars)

def main():
    for i in sys.argv[1:]:
        l,w,c = file_count()
        print(f"{l}\t{w}\t{c}\t{i}")


if __name__ == "__main__":
    main()
