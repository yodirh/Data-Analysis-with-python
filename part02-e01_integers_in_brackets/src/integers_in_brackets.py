#!/usr/bin/env python3

import re

'''def integers_in_brackets(s):
    List =[]
    a = re.sub(r"a[\d]+","ab", s)
    b = re.sub(r"[\d]+[+]","ab", a)
    c = re.sub(r"\+-[\d]+","ab", b)

    #a = re.findall(r"[\w+]+", s)
    d = re.findall(r"[-\d]+", c)
    for i in d:
        List.append(int(i))
    
    return List'''

def integers_in_brackets(s):
    result = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return list(map(int, result))


def main():
    m = integers_in_brackets(" afd [128+] [47 ] [a34] [ +-43 ]tt [+12]xxx!")
    print (m)

if __name__ == "__main__":
    main()
