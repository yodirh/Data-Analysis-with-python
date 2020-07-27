#!/usr/bin/env python3

def file_extensions(filename):
    List = []
    dick = {}
    f = open(filename, "r")
    #f = open("D:\DA Helsinki\ilenames.txt", "r")
    for i in f:
        if("." not in i):
            List.append(i.rstrip())
        else:
            j = i.rstrip().split(".")
            if j[-1] not in dick:
                dick[j[-1]] = [i.rstrip()]
            else:

             dick[j[-1]].append(i.rstrip())

    f.close()
    return (List,dick)

def main():
    i, j = file_extensions("src/filenames.txt")
    p =sorted(j.keys())
    
    print(f"{len(i)} files with no extension")
    for i in p:
        print(f"{i} {len(j[i])}")
    
            


if __name__ == "__main__":
    main()
