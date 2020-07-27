#!/usr/bin/env python3

def distinct_characters(L):
    char = {}
    for i in L:
        char[i] = len(set(i))
        
    return char


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
