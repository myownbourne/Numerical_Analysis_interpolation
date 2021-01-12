import numpy as np
from objfun import *


def equidistant_nodes(start,end,n,f):
    """
    Construct the data set including equidistant nodes in [start,end] and their function value.

    Arguments:
    n--size of the data set.
    start--begin of the range.
    end--end of the range. 
    f--choose objtive function.(f==1 y=|x|+1/(1+25*x*x), f==2 y=x/(1+x**4), f==3 y=arctan(x))

    Return:
    data--numpy array[[x0,y0],...,[xn,yn]], xi=start+ih(i=0,1,...,n), h=1/n.
    """
    h=(end-start)/n
    data=np.zeros((n+1,2))
    if f==1:
        objfun=objfun1
    elif f==2:
        objfun=objfun2
    elif f==3:
        objfun=objfun3

    for i in range(n+1):
        xi=start+i*h
        yi=objfun(xi)
        data[i][0]=xi
        data[i][1]=yi
    return data

def Chebyshev_nodes(n,f):
    """
    Construct the data set including Chebyshev nodes in [start,end] and their function value.

    Arguments:
    n--size of the data set.
    f--choose objtive function.(f==1 y=|x|+1/(1+25*x*x), f==2 y=x/(1+x**4), f==3 y=arctan(x))

    Return:
    data--numpy array[[x0,y0],...,[xn,yn]], xi=start+ih(i=0,1,...,n), h=1/n.
    """
    data=np.zeros((n+1,2))
    if f==1:
        objfun=objfun1
    elif f==2:
        objfun=objfun2
    elif f==3:
        objfun=objfun3

    for i in range(n+1):
        xi=5*np.cos(np.pi*(2*i+1)/(2*n+2))
        yi=objfun(xi)
        data[i][0]=xi
        data[i][1]=yi
    return data

def twoD_data(n):
    """
    Construct the data set on 2D plane.

    Arguments:
    n--size of the data set.
    start--begin of the range.
    end--end of the range. 
    f--choose objtive function.(f==1 y=|x|+1/(1+25*x*x), f==2 y=x/(1+x**4), f==3 y=arctan(x))

    Return:
    data--dictionary {'x':x,'y':y,'z':z}, x=[x0,x1,...,xn], y=[y0,y1,...,ym], z numpy array [[[x0,y0],...,[x0,ym]],...,[[xn,y0],...,[xn,ym]]] 
    """
    h=4/n
    x=np.arange(-2,2.1,h)
    y=np.arange(-2,2.1,h)
    n=len(x)
    m=len(y)
    f=np.zeros((n,m))
    index=0
    for i in range(len(x)):
        for j in range(len(y)):
            f[i][j]=objfun4(x[i],y[j])
    data={'x':x,'y':y,'f':f}
    return data