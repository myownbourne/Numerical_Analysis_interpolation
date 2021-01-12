import numpy as np
from data_construction import *
from Lagrange_Interpolation import *
import matplotlib.pyplot as plt
from objfun import *
import math

def Aitken_Interpolation_Polynomial(x,data):
    """
    Construct Aitken interpolation polynomial.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--The given set of points [[x_0,y_0],...,[xn,yn]].

    Return:
    table[-1][-1]--Function value on the specified node.
    """
    n=data.shape[0] #n=5
    table=np.zeros((n,n+1))
    table[:,0]=data[:,0]
    table[:,1]=data[:,1]
    for j in range(2,n+1):
        for i in range(j-1,n):
            table[i][j]=table[j-2][j-1]+(table[i][j-1]-table[j-2][j-1])*(x-table[j-2][0])/(table[i][0]-table[j-2][0])
    return table[-1][-1]



