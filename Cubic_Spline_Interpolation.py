from Newton_Interpolation import *
import matplotlib.pyplot as plt
import numpy as np

def cubic_spline_function(x,data,s0,sn):
    """
    Construct cubic spline function.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--The given set of points [[x_0,y_0],...,[xn,yn]].
    s0--S'(x_0)
    sn--S'(x_n)

    Return:
    result--Function value on the specified node.
    """
    if x>=data[-1][0]:
        return data[-1][1]
    x_data=data[:,0] #0-n
    y_data=data[:,1] #0-n
    n=len(x_data)-1
    h=x_data[1:]-x_data[0:-1] #0-(n-1)
    u_=h[0:-1]/(h[0:-1]+h[1:])
    u=np.concatenate((u_,[1]))
    lam_=1-u_
    lam=np.concatenate(([1],lam_))
    mat=np.diag([2] * (n+1))+np.diag(u,k=-1)+np.diag(lam,k=1)

    p=Difference_Quotient(data)
    d_=6*p[2:, 3]
    d0=(6/h[0])*(p[1][2]-s0)
    dn=(6/h[-1])*(sn-p[n][2])
    d=np.concatenate(([d0],d_,[dn]))

    M=np.linalg.solve(mat,d)
    for i in range(len(data)):
        if (data[i][0]<=x and data[i+1][0]>=x):
            index=i
            break

    Mi=M[i]
    Mip1=M[i+1]
    xi=data[i][0]
    xip1=data[i+1][0]
    fi=data[i][1]
    fip1=data[i+1][1]
    hi=h[i]
    result=Mi*(xip1-x)**3/(6*hi)+Mip1*(x-xi)**3/(6*hi)+(fi-Mi*hi**2/6)*(xip1-x)/hi+(fip1-Mip1*hi**2/6)*(x-xi)/hi
    return result

