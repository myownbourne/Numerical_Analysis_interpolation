import numpy as np

def Lagrange_Interpolation_Polynomial(x,data):
    """
    Construct Lagrange interpolation polynomial.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--The given set of points [[x_0,y_0],...,[xn,yn]].

    Return:
    result--Function value on the specified node.
    """
    result=0
    for i in range(len(data)):
        li=1
        for j in range(len(data)):
            if j==i:
                continue
            li=li*(x-data[j][0])
        for k in range(len(data)):
            if k==i:
                continue
            li=li/(data[i][0]-data[k][0])
        result+=li*data[i][1]
    return result
