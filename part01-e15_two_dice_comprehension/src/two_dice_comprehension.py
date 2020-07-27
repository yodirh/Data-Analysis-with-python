#!/usr/bin/env python3

def main():
    

    s = {"({},{})".format(a,b) for a in range(1,7) for b in range(1,7) if a+b ==5 } 
    for i in s:
        print (i)
    #better way
    #print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))

if __name__ == "__main__":
    main()
