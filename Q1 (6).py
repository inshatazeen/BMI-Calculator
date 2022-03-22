# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:26:37 2021

@author: insha Tazeen
"""

def main():
    file1=open("input.txt", "a")
    file2=open("bmi.txt", "a")

    #Enter your name and then print it
    Name = input("Enter the your name")
    print("Name is:", Name, file=file1)
    #We have to find the height in centimeter and then print it
    Height = float(input("Enter your Height in centimeters:"))
    print("Height is:", Height, file=file1)
    #Weight is to be inputed and then printed
    Weight = float(input("Enter your Weight in kilograms:"))
    print("Weight is:", Weight, file=file1)

    print("\n",file=file1)
    #divide the height from meters to centimeters
    Height = Height/100
    #Calculate the BMI formula
    BMI = float(Weight/(Height*Height))
    C = round(BMI,2)

    print("The BMI is:", C, file=file2)
    # if C is lesser than 18.5 then the individual is underweight
    if C < 18.5:
        file2.write("Underweight\n")
        file2.write("\n")
    # if C is greater than 18.5 and smaller than 25 print normal
    elif C >= 18.5 and C < 25:
        file2.write("Normal\n")
        file2.write("\n")
    # if C is greater than 25 but smaller than 30 then you are overweight
    elif C >= 25 and C < 30:
        file2.write("Overweight\n")
        file2.write("\n")
    #else if the C is more than you have to print obese
    else:
        file2.write("Obesity\n")
        file2.write("\n")



    file1.close()
    file2.close()




main()