import numpy as np

def composite_integration_rule(data):
    """
    Numerical integration
    Arguments:
    data--numpy array including nodes and function values [[x0,y0],...,[xn,yn]].

    Return:
    T--result.
    """
    T=0
    T+=data[-1][1]
    T+=data[0][1]
    h=data[1][0]-data[0][0]
    n=len(data)
    for i in range(1,n-1):
        T+=2*data[i][1]
    T=T*h/2
    return T
