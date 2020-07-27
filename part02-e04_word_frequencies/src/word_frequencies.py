#!/usr/bin/env python3

def word_frequencies(filename = "src/alice.txt"):
    d = {}
    #f = open("D:\lice.txt","r")
    f = open(filename, "r")
    for i in f:
        j =i.split()
        for i in j:
            k=i.strip("""!"#$%&'()*,-./:;?@[]_""")
            if k in d:
                d[k] +=1
            else:
                d[k] = 1

    f.close()

    return d
def main():
    print(word_frequencies())
    '''for word, count in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{count}")'''

if __name__ == "__main__":
    main()
