# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:58:25 2021

@author: Insha Tazeen
"""

# first we need to put a function to read  the file
def readFile():
    x = file1.read()

    print(x)

# Then we need to input the Function for  count total number of tokens
def countTokens():
    i = file1.read()
    k = i.split()

    print("The total number of tokens in the file are:", len(k))

# Next is to input the Function to find  the frequency of a particular token in the file.
def countToken(str1):
    s = file1.read()
    COUNT = s.count(str1)
    
    print("The frequency of", str1, "is:", COUNT)



# then we need to put a Function to find  the normalised frequency of a particular token in the file..
def normalisedFrequency(str2):
    h = file1.read()
    g = h.lower()
    p = h.split()

    count = g.count(str2)

    print("The normalised frequency of", str2, "is:", count/len(p))
    

# Next we need to input the Function to find  the total number of sentences in the file.
def sentenceCount():
    l = list(file1)
    w = 0

    for i in l:
        w = w + len(i.split('.'))

    print("The total number of sentences in the file are:", w)



# Then we need to insert the Function to find  the sentence containing words in the file
def sentenceContaining(str3):
    m = []

    n = file1.read()
    for i in n.split('\n'):
        if str3 in i.lower():
            m.append(i.strip())
    print(m)
   




while True:
    
    filename = input("Enter the file name to read:")
    file1 = open(filename,"r")


    print("\nMAIN MENU")
    print("1. Read the  file")
    print("2. Token  the Count")
    print("3. Frequency of the  particular token")
    print("4.  The Normalised Frequency")
    print("5.  The Sentence Count")
    print("6.  The Sentence Containing")
    print("7. Exit")
    choice = int(input("Enter your choice"))

    if choice == 1:
        readFile()
    elif choice == 2:
        countTokens()
    elif choice == 3:
        print("Enter the token to find frequency")
        token1 = input()
        countToken(token1)
    elif choice == 4:
        print("Enter the token to find normalised frequency")
        token2 = input()
        normalisedFrequency(token2)
    elif choice == 5:
        sentenceCount()
    elif choice == 6:
        print("Enter the token to find the sentence:")
        token3 = input()
        sentenceContaining(token3)
    else:
        break

    file1.close()

#Frequency of a particular token so the token used is (the)
#Normalised frequency token used is (motion)
#Sentence containing token used is (Important)
