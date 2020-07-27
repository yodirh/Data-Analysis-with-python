#!/usr/bin/env python3

def find_matching(L, pattern):
    
    li = []
    counter =0
    for i, x in enumerate(L): 
        if(pattern in x):
            li.append(counter)
        counter+=1
    return li

def main():
    print (find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
