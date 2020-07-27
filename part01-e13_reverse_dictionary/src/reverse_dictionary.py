#!/usr/bin/env python3

def reverse_dictionary(d):
    f= {}
    for key in d:
        for g in d.get(key):
            
            if g in f:
                for i in f.get(g):
                    f[g]=[i,key]
                
            else:
                f[g] = [key]
        
    return f

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa','salata'], 'six': ['kuusi'], 'fir': ['kuusi']}

    print (reverse_dictionary(d))

if __name__ == "__main__":
    main()
