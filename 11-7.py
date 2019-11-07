from scipy.integrate import odeint
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['p','r','b','alphac1','alphac2'])
t = np.arange(0, 30, 0.01)

def abs_average(a):
    sum = 0
    for i in a:
        sum += np.abs(i)
    return sum/len(a)

def lorenz(w,t,p,r,b,alpha):
    x1,x2,x3,y1,y2,y3 = w
    return np.array([-p*x1+p*x2, r*x1-x2-x1*x3, x1*x2-b*x3,\
                     -p*y1+p*x2*(1+alpha), r*y1-y2-y1*y3, y1*y2-b*y3])

def find_alphac(args=[10,28,3], x0=[2.0,0.0,0.0], y0=[50.0,50.0,30.0]):
    
    alpha = np.linspace(0,-0.2,40)
    
    for i in alpha:
        track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], i))
        delta1 = track[:,0] - track[:,3]
        delta2 = track[:,1] - track[:,4]
        if abs_average(delta1[-100:])<1 and abs_average(delta2[-100:])<1:
            continue
        else:
            alphac1 = i
            break
    
    alpha = np.linspace(0,0.2,40)
    for i in alpha:
        track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], i))
        delta1 = track[:,0] - track[:,3]
        delta2 = track[:,1] - track[:,4]
        if abs_average(delta1[-100:])<1 and abs_average(delta2[-100:])<1:
            continue
        else:
            alphac2 = i
            break
    
    global df
    new_df = pd.DataFrame({'p':[args[0]],'r':[args[1]],'b':[args[2]],'alphac1':[alphac1],'alphac2':[alphac2]})
    df = df.append(new_df)

num = 0

prb = []
for i in np.linspace(2,22,100):
    prb.append([i,28,8/3])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/100)

'''

prb = []
for i in np.linspace(24,26,1000):
    prb.append([10,i,3])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/1000)

prb = []
for i in np.linspace(0,100,1000):
    prb.append([10,28,i])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/1000)
'''

df.to_csv('test.csv')
