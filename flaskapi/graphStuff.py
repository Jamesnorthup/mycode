#!/usr/bin/python3

import numpy as np # number operations
import yaml # pyyaml for yaml
import re  # regex
import paramiko # ssh into servers
from flask import Flask, render_template
import matplotlib.pyplot as plt


import sympy as sym
from sympy import *
from spb import *
import numpy as np
import pandas as pd
import sympy
import cmath
from sympy import lambdify
import numpy as np
from IPython.display import display
import yaml
from sympy.plotting import plot


def sshlogin(ip, un, passw):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=ip, username=un, password=passw)
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    sshresult = ssh_stdout.read().decode('utf-8').split()[0]
    with open("sshresult", "w") as myfile:
        myfile.write(sshresult)
    days = (int(float(sshresult)) / 86400)  # convert uptime in sec to days
    sshsession.close()
    print(days)
    return days

app = Flask(__name__)

@app.route("/graphin")
def graphin():
    with open("/home/student/sshpass.yml") as sshpass: # creds for our servers
        creds = yaml.load(sshpass)
    svruptime = []
    xtick = []
    for cred in creds:
        xtick.append(cred['ip'])
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        svruptime.append(resp)
    xtick = tuple(xtick) # create a tuple
    svruptime = tuple(svruptime)
    Graph_userInput()
    return render_template("graph.html")


def getDisplayText():
    with open("AppResponsesLabels.yaml","r") as pod:
        displayTxt = yaml.load(pod, Loader=yaml.FullLoader)
    return displayTxt


displayTxt=getDisplayText()


def PlotXY():
    userInput = input(displayTxt["EXAMPLE_RP_TEXT"])
    Rg=list(map(int,input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]
    x=Symbol('x')
    FN = sym.sympify(userInput)
    display(FN)

    plot(FN, show=True, xlim=(Rg[0],Rg[1]), ylim=(Rg[2],Rg[3]), xlabel="",ylabel="").save('static/XYGraph.pdf')
    
    


def PlotComplexVector():
    z = Symbol('z')
    expr = sympify(input(displayTxt["EXAMPLE_CV_TEXT"]))
    Rg=list(map(int,input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]
    #GraphAxis =  Range_x_y[0] + Range_x_y[1]*(0+1j)
   
    display(expr)
    plot_complex_vector(expr, (z, Rg[0]+Rg[2]*(0+1j), Rg[1]+Rg[3]*(0+1j)),
        "Magnitude of %s" % str(expr), scalar=False, streamlines=True).save('static/ComplexVectorGraph.pdf')

def PlotComplexAbsoulteValue():
    z = Symbol('z')
    expr = sympify(input(displayTxt["EXAMPLE_CA_TEXT"]))
    Rg=list(map(int,input(displayTxt["RANGE_XY_TEXT"]).strip().split()))[:4]

   
    display(expr)

    
    plot_real_imag(expr, (z, Rg[0]+Rg[2]*(0+1j), Rg[1]+Rg[3]*(0+1j)),
    n=100, real=False, imag=False, abs=True, threed=True).save('static/ComplexAbsoluteGraph.pdf')

def Graph_userInput():
    

    cont = True

    while cont:
   
        
        print(displayTxt["CHOOSE_TEXT"], flush=True)
        userInput = input().lower()
        try:
            if(userInput=="h"):
                print(displayTxt["HELP_TEXT"])
            elif(userInput=="q"):
                cont=False
            elif (userInput=="s"):

                PlotXY()
            elif (userInput=="cv"):
        
                PlotComplexVector()
            elif (userInput=="cab"):
                PlotComplexAbsoulteValue()
            
            else:
                print(displayTxt["INVALID_TEXT"])
          
        except Exception as e:
            print(displayTxt["ERROR_TEXT"],e, sep="\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


