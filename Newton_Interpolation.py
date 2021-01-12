import numpy as np

def Difference_Quotient(data):
    """
    Calculate the difference quotient table.

    Arguments:
    data--numpy array including nodes and function values [[x0,y0],...,[xn,yn]].

    Return:
    table--the difference quotient table.
    
    """
    n=data.shape[0]
    x=data[:,0]
    y=data[:,1]
    table=np.zeros((n,n+1))
    table[:,0]=data[:,0]
    table[:,1]=data[:,1]
    for j in range(2,n+1):
        table[j-1: n, j]=(table[j-1: n, j-1]-table[j-2: n-1, j-1])/(x[j-1: n]-x[:n+1-j])
    return table

def Newton_Interpolation_Polynomial(x,data):
    """
    Construct Newton interpolation polynomial.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--The given set of points [[x0,y0],...,[xn,yn]].

    Return:
    result--Function value on the specified node.
    """
    n=data.shape[0]
    table=Difference_Quotient(data)
    dq=np.diag(table, k=1)
    result=dq[0]
    for i in range(1,n):
        temp=dq[i]
        for j in range(i):
            temp*=(x-data[j][0])
        result+=temp
    return result

