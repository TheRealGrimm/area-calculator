#initialise set-up
import math

calculate = True
shape = ""
answer = ""

while calculate:
    area = 0
    while shape.upper() != "A" and shape.upper() != "B" and shape.upper() != "C" and shape.upper() != "D" and shape.upper() != "E":
        shape = input("What shape do you want to calculate the area of? Type the letter. /nA. Right-angled triangle/nB. Non right-angled triangle/nC. Square/nD. Rectangle/nE. Circle/n")
        if shape.upper() != "A" and shape.upper() != "B" and shape.upper() != "C" and shape.upper() != "D" and shape.upper() != "E":
            print("Not a valid choice.")
    
    if shape.upper == "A":
        base = float(input("What is the length of the base of the triangle in cm? "))
        height = float(input("What is the length of the perpendicular height of the triangle in cm? "))
        area = (base * height) / 2
    elif shape.upper() == "B":
        sideA = float(input("What is the length of one side of this triangle in cm? "))
        sideB = float(input("What is the length of another side of this triangle in cm? "))
        angle_degrees = float(input("What is the angle between these two sides in degrees? "))
        angle_radians = math.radians(angle_degrees)
        area = (sideA * sideB * math.sin(angle_radians)) / 2
    elif shape.upper() == "C":
        side = float(input("What is the length of a side of the square in cm? "))
        area = side**2
    elif shape.upper() == "D":
        length = float(input("What is the length of the triangle in cm? "))
        width = float(input("What is the width of the triangle in cm? "))
        area = length * width
    elif shape.upper() == "E":
        radius = float(input("What is the length of the radius of the circle in cm? "))
        area = math.pi * (radius**2)
    
    if shape.upper() == "A" or shape.upper == "B":
        print(f"The area of the triangle is {area} cm\u00b2.")
    elif shape.upper() == "C":
        print(f"The area of the square is {area} cm\u00b2.")
    elif shape.upper() == "D":
        print(f"The area of the rectangle is {area} cm\u00b2.")
    elif shape.upper() == "E":
        print(f"The area of the circle is {area} cm\u00b2.")
    
    while answer.lower() != "yes" and answer.lower() != "no":
        answer = input("Do you want to calculate the area of another shape? ")
        if answer.lower() != "yes" and answer.lower() != "no":
            print("Invalid answer.")
        elif answer.lower() == "no":
            calculate = False
