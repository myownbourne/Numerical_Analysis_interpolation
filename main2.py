from Lagrange_Interpolation import *
from objfun import *
from data_construction import *
from Newton_Interpolation import *
import matplotlib.pyplot as plt
from Piecewise_Linear_Interpolation import *
from Cubic_Spline_Interpolation import *
from Bezier_curve import *
from Aitken_Interpolation import *
import time

def main():
    #1.y=|x|+1/(1+25*x*x) x in [-5,5]
    data10=equidistant_nodes(-5,5,10,1)
    data16=equidistant_nodes(-5,5,16,1)
    data20=equidistant_nodes(-5,5,20,1)
    print('Difference Quotient Table')
    print(Difference_Quotient(data10).round(2))
    x=np.arange(-5,5.01,0.01)

    y10=Newton_Interpolation_Polynomial(x,data10)
    y16=Newton_Interpolation_Polynomial(x,data16)
    y20=Newton_Interpolation_Polynomial(x,data20)
    y_true=objfun1(x)

    f, ax = plt.subplots(2, 2)
    plt.tight_layout() 
    f.suptitle('Newton y=|x|+1/(1+25*x*x), x in [-5,5]',fontsize=9,color='b',x=0.52,y=0.51)
    ax[0][0].plot(x,y_true,'b')
    ax[0][1].plot(x,y_true,'b')
    ax[0][1].plot(x,y10,'r')
    ax[1][0].plot(x,y_true,'b')
    ax[1][0].plot(x,y16,'r')
    ax[1][1].plot(x,y_true,'b',label='objective function')
    ax[1][1].plot(x,y20,'r',label='Newton polynomial')
    ax[0][0].set_title('objfun',fontsize=9,color='r')
    ax[0][1].set_title('n=10',fontsize=9,color='r')
    ax[1][0].set_title('n=16',fontsize=9,color='r')
    ax[1][1].set_title('n=20',fontsize=9,color='r')
    plt.legend
    plt.show()

def main1():
    #2.y=|x|+1/(1+25*x*x) x in [-5,5], Chebyshev nodes
    data10_1=Chebyshev_nodes(10,1)
    data20_1=Chebyshev_nodes(20,1)
    data50_1=Chebyshev_nodes(50,1)
    x1=np.arange(-5,5.01,0.01)

    y10_1=Lagrange_Interpolation_Polynomial(x1,data10_1)
    y20_1=Lagrange_Interpolation_Polynomial(x1,data20_1)
    y50_1=Lagrange_Interpolation_Polynomial(x1,data50_1)
    y_true_1=objfun1(x1)

    f, ax = plt.subplots(2, 2)
    plt.tight_layout() 
    f.suptitle('Chebyshev nodes y=|x|+1/(1+25*x*x), x in [-5,5]',fontsize=9,color='b',x=0.52,y=0.51)
    ax[0][0].plot(x1,y_true_1,'b')
    ax[0][1].plot(x1,y10_1,'r')
    ax[0][1].plot(x1,y_true_1,'b')
    ax[1][0].plot(x1,y20_1,'r')
    ax[1][0].plot(x1,y_true_1,'b')
    ax[1][1].plot(x1,y50_1,'r',label='Lagrange Polynomial')
    ax[1][1].plot(x1,y_true_1,'b',label='objective function')
    ax[0][0].set_title('objfun',fontsize=9,color='r',x=0.4)
    ax[0][1].set_title('n=10',fontsize=9,color='r',x=0.6)
    ax[1][0].set_title('n=20',fontsize=9,color='r',x=0.4)
    ax[1][1].set_title('n=50',fontsize=9,color='r',x=0.6)
    plt.legend()
    plt.show()

    print()
    print('y=|x|+1/(1+25*x*x), x in [-5,5], using Chebyshev nodes, when x = 4.85:')
    print()
    print('n   f(4.85)  L_n(4.85)   error')
    f1=objfun1(4.85)
    L10_1=Lagrange_Interpolation_Polynomial(4.85,data10_1)
    L20_1=Lagrange_Interpolation_Polynomial(4.85,data20_1)
    L50_1=Lagrange_Interpolation_Polynomial(4.85,data50_1)
    print('---------------------------------')
    print(10,'%.3e' % f1,'%.3e' % L10_1,'%.3e' % abs(f1-L10_1))
    print('---------------------------------')
    print(20,'%.3e' % f1,'%.3e' % L20_1,'%.3e' % abs(f1-L20_1))
    print('---------------------------------')
    print(50,'%.3e' % f1,'%.3e' % L50_1,'%.3e' % abs(f1-L50_1))
    print('---------------------------------')

def main2():
    def S(x,N):
        #N--Total number of interpolation nodes
        return 5*np.cos((0.2*N*(x+5)+1)*np.pi/(2*N+2))

    data10_2=equidistant_nodes(-5,5,10,1)
    data20_2=equidistant_nodes(-5,5,20,1)
    data50_2=equidistant_nodes(-5,5,50,1)
    data10_2[:,0]=S(data10_2[:,0],10)
    data20_2[:,0]=S(data20_2[:,0],20)
    data50_2[:,0]=S(data50_2[:,0],50)
    x2=np.arange(-5,5.01,0.01)

    y10_2=Lagrange_Interpolation_Polynomial(S(x2,10),data10_2)
    y20_2=Lagrange_Interpolation_Polynomial(S(x2,20),data20_2)
    y50_2=Lagrange_Interpolation_Polynomial(S(x2,50),data50_2)
    y_true_2=objfun1(x2)

    f, ax = plt.subplots(2, 2)
    plt.tight_layout() 
    f.suptitle('S-Runge',fontsize=9,color='b',x=0.52,y=0.51)
    ax[0][0].plot(x2,y_true_2,'b')
    ax[0][1].plot(x2,y10_2,'r')
    ax[0][1].plot(x2,y_true_2,'b')
    ax[1][0].plot(x2,y20_2,'r')
    ax[1][0].plot(x2,y_true_2,'b')
    ax[1][1].plot(x2,y50_2,'r',label='Lagrange Polynomial')
    ax[1][1].plot(x2,y_true_2,'b',label='objective function')
    ax[0][0].set_title('objfun',fontsize=9,color='r')
    ax[0][1].set_title('n=10',fontsize=9,color='r')
    ax[1][0].set_title('n=20',fontsize=9,color='r')
    ax[1][1].set_title('n=50',fontsize=9,color='r')
    plt.legend()
    plt.show()

def main3():
    data10_3=equidistant_nodes(-5,5,10,1)
    data20_3=equidistant_nodes(-5,5,20,1)
    x3=np.arange(-5,5.01,0.01)

    y10_3=np.zeros_like(x3)
    y20_3=np.zeros_like(x3)
    for i in range(len(y10_3)):
        y10_3[i]=Piecewise_Linear_Interpolation_Function(x3[i],data10_3)
    for i in range(len(y20_3)):
        y20_3[i]=Piecewise_Linear_Interpolation_Function(x3[i],data20_3)
    y_true_3=objfun1(x3)

    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8,4))
    plt.tight_layout() 
    fig.suptitle('Piecewise Linear y=|x|+1/(1+25*x*x), x in [-5,5]',fontsize=9,color='b',y=0.99)
    ax1.plot(x3,y_true_3,'r',label='Lagrange Polynomial')
    ax1.plot(x3,y10_3,'b',label='objective function')
    ax2.plot(x3,y_true_3,'r',label='Lagrange Polynomial')
    ax2.plot(x3,y20_3,'b',label='objective function')
    ax1.set_title('n=10',fontsize=9,color='r')
    ax2.set_title('n=20',fontsize=9,color='r')
    plt.legend()
    plt.show()

    print()
    print('y=|x|+1/(1+25*x*x), x in [-5,5],piecewise linear interpolation, when x = 4.85:')
    print()
    print('n   f(4.85)   P(4.85)   error')
    f3=objfun1(4.85)
    L10_3=Piecewise_Linear_Interpolation_Function(4.85,data10_3)
    L20_3=Piecewise_Linear_Interpolation_Function(4.85,data20_3)
    print('---------------------------------')
    print(10,'%.3e' % f3,'%.3e' % L10_3,'%.3e' % abs(f3-L10_3))
    print('---------------------------------')
    print(20,'%.3e' % f3,'%.3e' % L20_3,'%.3e' % abs(f3-L20_3))
    print('---------------------------------')

def main4():
    data30=equidistant_nodes(-5,5,30,1)
    data50=equidistant_nodes(-5,5,50,1)
    test=np.arange(-5,5.01,0.01)

    time_start1=time.time()
    y1=Newton_Interpolation_Polynomial(test,data30)
    time_end1=time.time()
    time1=time_end1-time_start1

    time_start2=time.time()
    y2=Lagrange_Interpolation_Polynomial(test,data30)
    time_end2=time.time()
    time2=time_end2-time_start2

    time_start3=time.time()
    y3=Newton_Interpolation_Polynomial(test,data50)
    time_end3=time.time()
    time3=time_end3-time_start3

    time_start4=time.time()
    y2=Lagrange_Interpolation_Polynomial(test,data50)
    time_end4=time.time()
    time4=time_end4-time_start4

    print()
    print('computational complexity of 2 method in s')
    print()
    print('n   Newton  Lagrange')
    print('------------------------')
    print(30,'%f' %time1,'%f' %time2)
    print('------------------------')
    print(50,'%f' %time3,'%f' %time4)
    print('------------------------')

    #plt.plot(test,y1,'r')
    #plt.plot(test,y2,'b')
    #plt.show()

def main5():
    data10_5=equidistant_nodes(-0.5,0.5,10,1)
    data20_5=equidistant_nodes(-0.5,0.5,20,1)
    x5=np.arange(-0.5,0.51,0.01)
    y10_5=np.zeros_like(x5)
    y20_5=np.zeros_like(x5)
    y_true_5=objfun1(x5)
    for i in range(len(y10_5)):
        y10_5[i]=cubic_spline_function(x5[i],data10_5,-1,1)
    for i in range(len(y20_5)):
        y20_5[i]=cubic_spline_function(x5[i],data20_5,-1,1)

    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8,4))
    plt.tight_layout() 
    fig.suptitle('Cubic spline interpolation y=|x|+1/(1+25*x*x), x in [-0.5,0.5]',fontsize=9,color='b',y=0.99)
    ax1.plot(x5,y_true_5,'r')
    ax1.plot(x5,y10_5,'b')
    ax2.plot(x5,y_true_5,'r',label='Cubic Spline Polynomial')
    ax2.plot(x5,y20_5,'b',label='objective function')
    ax1.set_title('n=10',fontsize=9,color='r',x=0.4)
    ax2.set_title('n=20',fontsize=9,color='r',x=0.6)
    plt.legend(loc='lower right')
    plt.show()

def main6():
    data10_6=equidistant_nodes(-0.5,0.5,10,1)
    data20_6=equidistant_nodes(-0.5,0.5,20,1)
    x6=np.arange(-0.5,0.51,0.01)
    y_true_6=objfun1(x6)
    x61,y_10_6=Bezier_curve(data10_6)
    x62,y_20_6=Bezier_curve(data20_6)

    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8,4))
    plt.tight_layout() 
    fig.suptitle('bazier curve y=|x|+1/(1+25*x*x), x in [-0.5,0.5]',fontsize=9,color='b',y=0.99)
    ax1.plot(x61,y_10_6,'r')
    ax1.plot(x6,y_true_6,'b')
    ax2.plot(x62,y_20_6,'r',label='Bazier curve')
    ax2.plot(x6,y_true_6,'b',label='objective function')
    ax1.set_title('n=10',fontsize=9,color='r',x=0.4)
    ax2.set_title('n=20',fontsize=9,color='r',x=0.6)
    plt.legend(loc='lower right')
    plt.show()

def main7():
    data10_7=equidistant_nodes(-5,5,10,1)
    data16_7=equidistant_nodes(-5,5,16,1)
    data20_7=equidistant_nodes(-5,5,20,1)
    x7=np.arange(-5,5.01,0.01)
    y_10_7=np.zeros_like(x7)
    y_16_7=np.zeros_like(x7)
    y_20_7=np.zeros_like(x7)
    y_true_7=objfun1(x7)
    for i in range(len(x7)):
        y_10_7[i]=Aitken_Interpolation_Polynomial(x7[i],data10_7)
        y_16_7[i]=Aitken_Interpolation_Polynomial(x7[i],data16_7)
        y_20_7[i]=Aitken_Interpolation_Polynomial(x7[i],data20_7)
    
    f, ax = plt.subplots(2, 2)
    plt.tight_layout() 
    f.suptitle('Aitken y=|x|+1/(1+25*x*x), x in [-5,5]',fontsize=9,color='b',x=0.52,y=0.51)
    ax[0][0].plot(x7,y_true_7,'b')
    ax[0][1].plot(x7,y_true_7,'b')
    ax[0][1].plot(x7,y_10_7,'r')
    ax[1][0].plot(x7,y_true_7,'b')
    ax[1][0].plot(x7,y_16_7,'r')
    ax[1][1].plot(x7,y_true_7,'b',label='objective function')
    ax[1][1].plot(x7,y_20_7,'r',label='Aitken polynomial')
    ax[0][0].set_title('objfun',fontsize=9,color='r')
    ax[0][1].set_title('n=10',fontsize=9,color='r')
    ax[1][0].set_title('n=16',fontsize=9,color='r')
    ax[1][1].set_title('n=20',fontsize=9,color='r')
    plt.legend
    plt.show()

if __name__ == '__main__':
    main()
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()