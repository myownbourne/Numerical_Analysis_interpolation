import numpy as np
import math
import cv2

def bilinear(input,k1,k2):
    """
    Image magnification(bilinear)
    Arguments:
    input--original image.
    k1--row scale factor.
    k2--column sacle factor.

    Return:
    output--Function value on the specified node.
    """
    input_=np.copy(input) 
    input_m,input_n=input_.shape
    output_m=int(input_m*k1)
    output_n=int(input_n*k2)
    output=np.zeros((output_m, output_m))

    for i in range(output_m):
        for j in range(output_n):
            x=i/output_m*input_m
            y=j/output_n*input_n
            x1=int(x)
            y1=int(y)
            x2=x1
            y2=y1+1
            x3=x1+1
            y3=y1
            x4=x1+1
            y4=y1+1
            u=x-x1
            v=y-y1

            if x4>=input_m:
                x4=input_m-1
                x2=x4
                x1=x4-1
                x3=x4-1
            if y4>=input_n:
                y4=input_n-1
                y3=y4
                y1=y4-1
                y2=y4-1
            output[i, j] = int((1-u)*(1-v)*input_[x1, y1] + (1-u)*v*input_[x2, y2] + u*(1-v)*input_[x3, y3] + u*v*input_[x4, y4])
    return output

def NN(input,k1,k2):
    """
    Image magnification(nearest neighbor)
    Arguments:
    input--original image.
    k1--row scale factor.
    k2--column sacle factor.

    Return:
    output--Function value on the specified node.
    """
    input_=np.copy(input) 
    input_m,input_n = input_.shape
    output_m=int(input_m*k1)
    output_n=int(input_n*k2)

    output=np.zeros((output_m,output_n))
    for i in range(output_m):
        for j in range(output_n):
            x=round(i*input_m/output_m)
            y=round(j*input_n/output_n)
            if x>=input_m:
                x=input_m-1
            if y>=input_n:
                y=input_n-1
            output[i][j]=input_[x][y]
    return output
