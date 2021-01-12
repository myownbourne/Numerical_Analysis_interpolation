import numpy as np
from data_construction import *

def Piecewise_Linear_Interpolation_Function(x,data):
    """
    Construct piecewise linear interpolation function.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--The given set of points [[x_0,y_0],...,[xn,yn]].

    Return:
    result--Function value on the specified node.
    """
    #print(x)
    if x>data[-1][0]:
        return data[-1][1]
    for i in range(len(data)):
        #print(i,data[i][0])
        if (data[i][0]<=x and data[i+1][0]>=x):
            index=i
            break
    x1=data[index][0]
    y1=data[index][1]
    x2=data[index+1][0]
    y2=data[index+1][1]
    return y1*(x-x2)/(x1-x2)+y2*(x-x1)/(x2-x1)