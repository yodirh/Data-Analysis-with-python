#!/usr/bin/env python3

def triple(val):
    return val*3

def square(val):
    return val**2

def main():
    for i in range(1,11):
        a = triple(i)
        b= square(i)
        if b>a:
            break
        else:
             print("triple({})=={} square({})=={}".format(i,a,i,b))

       

if __name__ == "__main__":
    main()
