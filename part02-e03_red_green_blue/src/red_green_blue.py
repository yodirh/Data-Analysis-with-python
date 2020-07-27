#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    List =[]
    #g = "D:\cgb.txt"
    #f = filename
    #f = open(filename, "r")
   
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if line.strip("\n") != "! $Xorg: rgb.txt,v 1.3 2000/08/17 19:54:00 cpqbld Exp $":
                f.write(line)

    for i in lines:
        s = ""
        r = re.findall(r"\w+",i)
        for i,j in enumerate(r):
            if i <3:
                s +=str(j)+"\t"
            elif i>3:
                s +=" "+str(j)
            else:
                s +=str(j)
            
        List.append(s)
    return List
def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
