import numpy as np
from data_construction import *
from objfun import *

def Bezier_curve(data):
    """
    construct bazier curve.

    Arguments:
    data--The given set of points [[x_0,y_0],...,[xn,yn]].

    Return:
    result.T[0], result.T[1]--x and y.
    """
    date_x=data[:,0]
    date_y=data[:,1]

    mid = list()
    for i in range(1, date_x.shape[0]):
        mid.append({
            's':    (date_x[i-1], date_y[i-1]),
            'e':      (date_x[i], date_y[i]),
            'm':      ((date_x[i]+date_x[i-1])/2.0, (date_y[i]+date_y[i-1])/2.0)
        })
    
    split_points = list()
    for i in range(len(mid)):
        if i < (len(mid)-1):
            j = i+1
        else:
            continue
        
        x00, y00 = mid[i]['s']
        x01, y01 = mid[i]['e']
        x10, y10 = mid[j]['s']
        x11, y11 = mid[j]['e']
        d0 = np.sqrt(np.power((x00-x01), 2) + np.power((y00-y01), 2))
        d1 = np.sqrt(np.power((x10-x11), 2) + np.power((y10-y11), 2))
        split = 1.0*d0/(d0+d1)
        mx0, my0 = mid[i]['m']
        mx1, my1 = mid[j]['m']
        split_points.append({
            's':    (mx0, my0),
            'e':      (mx1, my1),
            'sp':    (mx0+(mx1-mx0)*split, my0+(my1-my0)*split)
        })
    cut= list()
    for i in range(len(split_points)):
        vx, vy = mid[i]['e'] 
        dx = vx - split_points[i]['sp'][0] 
        dy = vy - split_points[i]['sp'][1] 
        sx, sy = split_points[i]['s'][0]+dx, split_points[i]['s'][1]+dy
        ex, ey = split_points[i]['e'][0]+dx, split_points[i]['e'][1]+dy
        cp0 = sx+(vx-sx)*0.5, sy+(vy-sy)*0.5
        cp1 = ex+(vx-ex)*0.5, ey+(vy-ey)*0.5
        if cut:
            cut[-1].insert(2, cp0)
        else:
            cut.append([mid[0]['s'], cp0, mid[0]['e']])
        if i < (len(mid)-2):
            cut.append([mid[i+1]['s'], cp1, mid[i+1]['e']])
        else:
            cut.append([mid[i+1]['s'], cp1, mid[i+1]['e'], mid[i+1]['e']])
            cut[0].insert(1, mid[0]['s'])
    result = list()
    for item in cut:
        p0 = np.array(item[0])
        p1 = np.array(item[1])
        p2 = np.array(item[2])
        p3 = np.array(item[3])
        points = list()
        for t in np.linspace(0, 1, 12):
            points.append(p0*(1-t)**3 + 3*p1*t*(1-t)**2 + 3*p2*(1-t)*t**2 + p3*t**3)
        group=np.vstack(points)
        result.append(group[:-1])
    result.append(group[-1:])
    result= np.vstack(result)
    return result.T[0], result.T[1]

