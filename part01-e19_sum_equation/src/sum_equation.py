#!/usr/bin/env python3

def sum_equation(L):
    M = ""
    c = 0
    if(len(L)==0):
        M+= "0 = 0"
    else:
        for i in L:
            if(c==len(L)-1):
                M+=str(i) + " = "
            else:
                M+=str(i) + " + "
            c+=1
        M = M + str(sum(L))
    
    return M
#better way
"""if not L:
        return "0 = 0"
    result = list(map(str, L))
    return " + ".join(result) + f" = {sum(L)}"
"""
def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
