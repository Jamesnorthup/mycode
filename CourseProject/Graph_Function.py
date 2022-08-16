#!/usr/bin/env python3
### try except
import sympy as sym
from sympy import *
import numpy as np
import pandas as pd
import sympy
import cmath
import matplotlib.pyplot as plt
from sympy import lambdify
import numpy as np
from IPython.display import display
import yaml
import climage

def getDisplayText():
    with open("AppResponseLabels.yaml","r") as pod:
        displayTxt = yaml.load(pod, Loader=yaml.FullLoader)
    return displayTxt

def Help():
    
    print(displayTxt["HELP_TEXT"])
    
def PlotXY_DATA(userInput, Range_x_y):
#     userInput = input("Enter Function:  ")
    x=sym.Symbol('x')
    FN = sym.sympify(userInput)
    
    
    display(FN)

#     Range_x_y=list(map(int,input(displayTxt["RANGE_TEXT"]).strip().split()))[:2]
   
    x_List=np.array(list(range(Range_x_y[0],Range_x_y[1])))
    
    FN_R_Func= lambdify(x,FN,'numpy')
    y_List=FN_R_Func(x_List)
    
    df = pd.DataFrame({'x':x_List, 'y':y_List})
    df.to_csv("x_y_Function_Data", sep='\t')
    df.plot('x', 'y')
    plt.savefig('GRAPH.png') 
    print(climage.convert('GRAPH.png'))
def main():
    displayTxt=getDisplayText()

    cont = True

    while cont:
        x=sym.Symbol('x')
        
        print(displayTxt["CHOOSE_TEXT"])
        userInput = input().lower()
        
        if(userInput=="h"):
            print(displayTxt["HELP_TEXT"])
        elif(userInput=="q"):
            cont=False
        elif (userInput=="s"):
            userInput = input("Enter Function:  ")
            Range_x_y=list(map(int,input(displayTxt["RANGE_TEXT"]).strip().split()))[:2]
            PlotXY_DATA(userInput, Range_x_y)
        
if __name__ == "__main__":
    main()
