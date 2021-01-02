#!/usr/bin/env python3

def detect_ranges(L):
    k=sorted(L)
    b = []
    i= 0
    T=[]
    while (i<len(k)):

      if (i != len(k)-1 and k[i]+1 == k[i+1]):
        T.append(i)
        i +=1 

      elif (k[i]-1 == k[i-1] ):
        T.append(i)
        b.append((k[T[0]],k[T[-1]]+1))
        i+=1
        T.clear()
      else :
        b.append(k[i])
        i+=1
        T.clear()    
    return b

def main():
    L = [5,4,8,12,6,7,10,13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
