#!/usr/bin/env python3


def main():
    for i in range(1,11):
        for b in range(1,11):
            print("{:4d}".format(b*i), end="")
        print()
    

if __name__ == "__main__":
    main()
