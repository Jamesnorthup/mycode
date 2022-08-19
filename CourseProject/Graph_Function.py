#!/usr/bin/env python3


from sympy import *
from sympy.abc import x, z, t
from sympy.plotting import plot
from sympy.utilities.lambdify import implemented_function
from spb import *
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yaml

"""

Graphing App | James Northup

Application allows the user to input function and 
Range which is then saved. The application is able to 
graph mathematical complex and real functions. 

"""

# Returns data from yaml file which is used for
# for print out statements.
def getDisplayText():

    with open("AppResponseLabels.yaml", "r") as pod:
        displayTxt = yaml.load(pod, Loader=yaml.FullLoader)

    return displayTxt


def SaveData(x, displayTxt):
    # Get function from user.
    userInput = input(displayTxt["EXAMPLE_REAL_DATA_TEXT"])

    # Get range and interval from user.
    Rg = list(map(float, input(displayTxt["RANGE_REAL_DATA_TEXT"]).strip().split()))[:3]

    # Numpy array generated from range and interval input
    x_values = np.arange(Rg[0], Rg[1], Rg[2], dtype=float)

    # Sympy functional from user function
    f_x = sympify(userInput)

    # Display function
    display(f_x)

    # Sympy lambda function
    f = lambdify(x, f_x, "numpy")

    # Generate dataframe and store information into csv file
    pd.DataFrame({"x": x_values, "y": f(x_values)}).to_csv("FunctoinData.csv")


def PlotParametric(t, displayTxt):

    # Get two functions from user.
    userInput = list(
        map(str, input(displayTxt["EXAMPLE_PARA_TEXT"]).strip().split(","))
    )[:2]

    # Separte functions into sympy functional variables
    f_t = sympify(userInput[0])
    g_t = sympify(userInput[1])

    # Get range from user.
    Rg = list(map(float, input(displayTxt["RANGE_PARA_TEXT"]).strip().split()))[:2]

    # Plat parametric function
    plot_parametric((f_t, g_t), (t, Rg[0], Rg[1]))


def PlotXY(x, displayTxt):

    # Get function from user.
    f_x = sympify(input(displayTxt["EXAMPLE_RP_TEXT"]))

    # Get range from user.
    Rg = list(map(float, input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]

    # Display function.
    display(f_x)

    # Plot complex function.
    plot(
        f_x, show=True, xlim=(Rg[0], Rg[1]), ylim=(Rg[2], Rg[3]), xlabel="", ylabel=""
    ).save("XYGraph.pdf")


def PlotComplexVector(z, displayTxt):

    # Get function from user.
    f_z = sympify(input(displayTxt["EXAMPLE_CV_TEXT"]))

    # Get range from user.
    Rg = list(map(float, input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]

    # Display function.
    display(f_z)

    # Plot complex function.
    plot_complex_vector(
        f_z,
        (z, Rg[0] + Rg[2] * (0 + 1j), Rg[1] + Rg[3] * (0 + 1j)),
        "Magnitude of %s" % str(f_z),
        scalar=False,
        streamlines=True,
    ).save("ComplexVectorGraph.pdf")


# 3D graph of a complex function. The vertical of the graph represents coordinates absolute value.
def PlotComplexAbsoulteValue(z, displayTxt):

    # Get function from user.
    f_z = sympify(input(displayTxt["EXAMPLE_CA_TEXT"]))

    # Get range from user.
    Rg = list(map(float, input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]

    # Display function.
    display(f_z)

    # Plot complex function
    plot_real_imag(
        f_z,
        (z, Rg[0] + Rg[2] * (0 + 1j), Rg[1] + Rg[3] * (0 + 1j)),
        n=100,
        real=False,
        imag=False,
        abs=True,
        threed=True,
    ).save("ComplexAbsoluteGraph.pdf")


# Main Function
def main():

    # Get text data from yaml file
    displayTxt = getDisplayText()

    cont = True

    # Continues until user quits
    while cont:

        # Displays user chooses

        userInput = input(displayTxt["CHOOSE_TEXT"]).lower()

        # Selects function based on user choose. Chooses include graphing real and complex function
        # as well as storing functional data into csv file.
        try:

            if userInput == "h":

                print(displayTxt["HELP_TEXT"])

            elif userInput == "q":

                cont = False

            elif userInput == "sd":

                SaveData(x, displayTxt)

            elif userInput == "s":

                PlotXY(x, displayTxt)
            elif userInput == "p":

                PlotParametric(t, displayTxt)

            elif userInput == "cv":

                PlotComplexVector(z, displayTxt)

            elif userInput == "cab":

                PlotComplexAbsoulteValue(z, displayTxt)

            else:

                print(displayTxt["INVALID_TEXT"])

        except Exception as e:

            print(displayTxt["ERROR_TEXT"], e, sep="\n")


if __name__ == "__main__":
    main()
