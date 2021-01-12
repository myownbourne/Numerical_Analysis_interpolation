import matplotlib.pyplot as plt
from Cubic_Spline_Interpolation import *
from Piecewise_Linear_Interpolation import *
from Bezier_curve import *
from Numerical_Integration import *


def main(): 
    plt.plot(x, y1, 'bo')
    plt.plot(x, y2, 'bo')
    x_1_1,y_1_1=Bezier_curve(data1)
    x_1_2,y_1_2=Bezier_curve(data2)
    plt.plot(x_1_1, y_1_1,'r')
    plt.plot(x_1_2, y_1_2,'r')
    plt.title('Bazier curve')
    plt.show()

def main2():
    plt.plot(x, y1, 'bo')
    plt.plot(x, y2, 'bo')
    x2=np.arange(0,15.1,0.1)
    y_2_1=np.zeros_like(x2)
    y_2_2=np.zeros_like(x2)
    for i in range(len(x2)):
        y_2_1[i]=cubic_spline_function(x2[i],data1,0.6,-0.4)
    for i in range(len(x2)):
        y_2_2[i]=cubic_spline_function(x2[i],data2,0.4,0.6)

    plt.plot(x2,y_2_1,'r')
    plt.plot(x2,y_2_2,'r')
    plt.title('Cubic spline interpolation')
    plt.show()

def main3():
    plt.plot(x, y1, 'bo')
    plt.plot(x, y2, 'bo')
    x3=np.arange(0,15.1,0.1)
    y_3_1=np.zeros_like(x3)
    y_3_2=np.zeros_like(x3)
    for i in range(len(x3)):
        y_3_1[i]=Piecewise_Linear_Interpolation_Function(x3[i],data1)
    for i in range(len(x3)):
        y_3_2[i]=Piecewise_Linear_Interpolation_Function(x3[i],data2)

    plt.plot(x3,y_3_1,'r')
    plt.plot(x3,y_3_2,'r')
    plt.title('Piecewise linear interpolation')
    plt.show()

def main4():
    #method1_
    data0_3_1=data1[0:2,:]
    data0_3_2=data2[0:2,:]
    data3_11_1=data1[1:6,:]
    data3_11_2=data2[1:6,:]
    data11_15_1=data1[5:10,:]
    data11_15_2=data2[5:10,:]
    upper=composite_integration_rule(data0_3_1)+composite_integration_rule(data3_11_1)+composite_integration_rule(data11_15_1)
    lower=composite_integration_rule(data0_3_2)+composite_integration_rule(data3_11_2)+composite_integration_rule(data11_15_2)
    print('Numerical integration:')
    print('method1','%f'% (upper-lower))
    #method_2
    data_x=np.arange(0,15.1,0.1)
    data_y_1=np.zeros_like(data_x)
    data_y_2=np.zeros_like(data_x)
    for i in range(len(data_y_1)):
        data_y_1[i]=cubic_spline_function(data_x[i],data1,0.6,-0.4)
    for i in range(len(data_y_2)):
        data_y_2[i]=cubic_spline_function(data_x[i],data2,0.4,0.6)
    data_xy_1=np.vstack((data_x,data_y_1)).T
    data_xy_2=np.vstack((data_x,data_y_2)).T
    upper2=composite_integration_rule(data_xy_1)
    lower2=composite_integration_rule(data_xy_2)
    print('method2','%f' % (upper2-lower2))

if __name__ == '__main__':
    x=np.array([0,3,5,7,9,11,12,13,14,15])
    y1=np.array([0,1.8,2.2,2.7,3.0,3.1,2.9,2.5,2.0,1.6])
    y2=np.array([0,1.2,1.7,2.0,2.1,2.0,1.8,1.2,1.0,1.6])
    data1=np.vstack((x,y1)).T
    data2=np.vstack((x,y2)).T
    main()
    main2()
    main3()
    main4()