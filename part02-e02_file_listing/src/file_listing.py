#!/usr/bin/env python3

import re


def file_listing(filename ="src/listing.txt"):
    List = []
    #f = open("hy\hy-data-analysis-with-python-spring-2020\part02-e02_file_listing\src\listing.txt", "r")
    f = open(filename, "r")

    for i in f:
        r = re.findall(r"\d{1,7}", i)
        a = re.findall(r"[A-Z][a-z]+",i)[0]
        b =re.findall(r"[a-z]\w+\W\w+$|[a-z]+$|[a-z]+\W\w+\W\w+$|\W\w+$", i)[0]
        tup =(int(r[1]), a, int(r[2]), int(r[3]),int(r[4]),b )
        List.append(tup)
    f.close()
    
    return List

def main():

    print(file_listing())



if __name__ == "__main__":
    main()
