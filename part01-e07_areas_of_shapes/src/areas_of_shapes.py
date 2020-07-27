#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        inp = input("Choose a shape(triangle, rectangle, circle): ")
        if(inp == ""):
            break
        elif(inp == "triangle"):
            base=int(input("Give base of the triangle: "))
            height= int(input("Give the height of the triangle: "))
            print("The area is ", "%.6f" %(float(base*height)/2))
        elif(inp == "rectangle"):
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print("The area is ", "%.6f" %(float(width * height)))
        elif(inp == "circle"):
            radius = int(input("Give radius of the circle: "))
            print("The area is ", "%.6f" %(float(math.pi*radius**2)))
        else:
            print("Unknown shape!")



if __name__ == "__main__":
    main()
