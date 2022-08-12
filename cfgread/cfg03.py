#!/usr/bin/env python3
## create file object in "r"ead mode
fileName= input("Enter File Name:\n Example vlanconfig.cfg \n")



with open(fileName, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    fileSize = len(configlist)
    print("FileSize: ",fileSize, end="\n")
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

