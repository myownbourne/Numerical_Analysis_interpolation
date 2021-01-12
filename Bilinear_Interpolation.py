from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def Bilinear_Interpolation(x,y,data):
    """
    Construct bilinear interpolation polynomial.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--{'x':[x_0,...,xn],'y':[y_0,...,y_m],'f':[[f(x_0,y_0),...,f(x0,ym)],...,[f(x_n,y_0),...,f(x_n,y_m)]]}

    Return:
    result--Function value on the specified node.
    """
    for i in range(len(data['x'])-1):
        if data['x'][i]<=x and data['x'][i+1]>=x:
            index1=i
            break
    for j in range(len(data['y'])-1):
        if data['y'][j]<=y and data['y'][j+1]>=y:
            index2=j
            break
    Q11=data['f'][index1][index2]
    Q12=data['f'][index1][index2+1]
    Q21=data['f'][index1+1][index2]
    Q22=data['f'][index1+1][index2+1]
    x1=data['x'][index1]
    x2=data['x'][index1+1]
    y1=data['y'][index2]
    y2=data['y'][index2+1]
    return Q11*(x2-x)*(y2-y)/((x2-x1)*(y2-y1))+Q21*(x-x1)*(y2-y)/((x2-x1)*(y2-y1))+Q12*(x2-x)*(y-y1)/((x2-x1)*(y2-y1))+Q22*(x-x1)*(y-y1)/((x2-x1)*(y2-y1))

def NN_Interpolation(x,y,data):
    """
    Nearest neighbor interpolation.
    
    Arguments:
    x--Specified node that we want to know the function value.
    data--{'x':[x_0,...,xn],'y':[y_0,...,y_m],'f':[[f(x_0,y_0),...,f(x0,ym)],...,[f(x_n,y_0),...,f(x_n,y_m)]]}

    Return:
    result--Function value on the specified node.
    """
    for i in range(len(data['x'])-1):
        if data['x'][i]<=x and data['x'][i+1]>=x:
            if abs(data['x'][i]-x)<=abs(data['x'][i+1]-x):
                index1=i
            else:
                index1=i+1
            break
    for j in range(len(data['y'])-1):
        if data['y'][j]<=y and data['y'][j+1]>=y:
            if abs(data['y'][j]-y)<=abs(data['y'][j+1]-y):
                index2=j
            else:
                index2=j+1
            break
    return data['f'][index1][index2]


