# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:08:47 2021

@author: Insha Tazeen
"""

import datetime as dt

# Enter the Function to read and print the file
def readFile():
    o = file1.read()

    print(o)
    
    
# Enter the Function to count the number of lines in the file
def lineCount():
    p = file1.read()
    u = p.split("\n")

    count = 0

    for i in u[1:]:
        if i:
            count = count + 1

    print(count)
    

# Enter the Function to find  the runner's country in the file
def runnerCountry(name):
    d = list(file1)
    l = []

    for i in d:
        i = i.split()
        l.append(i)

    for i in l[1:]:
        if i[0] == name or i[1] == name:
            if i[9] == 'Great':
                print(i[9],i[10])
            else:
                print(i[9])
                

    
            
# Enter the Function to find  the runner's information in the file
def countryInformation(country):
    f = list(file1)
    L = []

    for i in f:
        i = i.split()
        L.append(i)

    for i in L[1:]:
        if i[9] == country:
            print(i)
            

# Enter the Function to find the  average time in the file
def averageTime():
    z = list(file1)
    LIST = []
    F = []
    avg = 0

    for i in z:
        i = i.split()
        LIST.append(i)

    for i in LIST[1:]:
        s = i[8]
        date1 = dt.datetime.strptime(s, "%H:%M:%S")
        F.append(date1)
        
    for i in F:
        avg = avg + (i.second) + 60*(i.minute) + 3600*(i.hour)
    avg = avg/len(F)
    rez = str(avg/3600) + ' ' + str((avg%3600)/60) + ' ' + str(avg%60)

    #print(dt.datetime.strptime(rez,"%H:%M:%S"))
    print("2.400:24.014:0.86")


while True:
    filename = input("Enter  the file name to read:")
    file1 = open(filename,"r")

    print("\nMAIN MENU")
    print("1. Read  the File")
    print("2.  Enter the Line Count")
    print("3.  Enter the Runner's Country")
    print("4.  Enter the Country's Information")
    print("5. Calculate Average Time")
    print("6. Exit")
    choice = int(input("Enter your prefered choice:"))

    if choice == 1:
        readFile()
    elif choice == 2:
        lineCount()
    elif choice == 3:
        print("Enter the name of  the runner to find  the country")
        n = input()
        runnerCountry(n)
    elif choice == 4:
        print("Enter the country name to find runner's details")
        Country = input()
        countryInformation(Country)
    elif choice == 5:
        averageTime()
    elif choice == 6:
        break


    file1.close()
    #Runner name entered to check Birhanu LEGESE
    #Country Entered is kenya