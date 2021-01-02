#!/usr/bin/env python3

def extract_numbers(s):
    new=[]
    splited = s.split()
    for i in splited:
        
        try:
            x = int(i)
            new.append(x)    
        except:
            try:
                x=float(i)
                new.append(x)
            except :
                pass

    return new

def main():
    print(extract_numbers("abc 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
