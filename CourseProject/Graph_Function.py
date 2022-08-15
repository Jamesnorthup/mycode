#!/usr/bin/env python3

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


def PlotXY_DATA(FN):
    x = sym.Symbol("x")
    x_range = input("Give range of x: Example -20, 20").split(",")
    x_min = int(x_range[0])
    x_max = int(x_range[1])

    x_List = np.array(list(range(x_min, x_max)))

    FN_R_Func = lambdify(x, FN, "numpy")
    y_List = FN_R_Func(x_List)

    df = pd.DataFrame({"x": x_List, "y": y_List})
    df.to_csv("x_y_Function_Data", sep="\t")
    df.plot("x", "y", kind="line")
    plt.title("Function Graph")
    plt.savefig("Function_Graph.png")
    return df


def main():

    x = sym.Symbol("x")
    y = sym.Symbol("y")
    print(
        "Methods:",
        "Integration: integrate()",
        "Differentiate: diff()",
        "Limit: limit",
        "SolveForRoot: root",
        sep="\n",
        end="\n\n",
    )
    print(
        "Variables include:\tx,y \nConstants include \nEulers e:\tE\nComplex i:\tI",
        flush=True,
    )

    Cont = True

    print("Type q to quit")
    inputFunction = input("Enter Function to be graphed")

    FN = sym.sympify(inputFunction)
    display(FN)
    PlotXY_DATA(FN)


if __name__ == "__main__":
    main()
