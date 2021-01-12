import numpy as np
import matplotlib.pyplot as plt
def objfun1(x):
    """
    Objtive function1 y= |x|+1/(1+25*x*x)
    """
    return np.abs(x)+1.0/(1.0+25*x*x)

def objfun2(x):
    """
    Objtive function y=x/(1+x^4)
    """
    return x/(1+x**4)

def objfun3(x):
    """
    Objtive function y=arctan(x)
    """
    return np.arctan(x)

def objfun4(x,y):
    """
    Objtive function y=(x+y)*e^((-5)*(x^2+y^2))
    """
    return (x+y)*np.exp(-5.0*(x**2 + y**2)) 



 
