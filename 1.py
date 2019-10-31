from scipy.integrate import odeint
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['p','r','b','alpha_c'])

alpha = 0
t = np.arange(0, 50, 0.01)

def lorenz(w,t,p,r,b):
    x1,x2,x3,y1,y2,y3 = w
    return np.array([-p*x1+p*x2, r*x1-x2-x1*x3, x1*x2-b*x3,\
                     -p*y1+p*x2*(1+alpha), r*y1-y2-y1*y3, y1*y2-b*y3])

def func1(args=[10,28,3], x0=[50.0,50.0,50.0], y0=[10.0,10.0,10.0]):
    track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2]))
    delta1 = track[:,0] - track[:,3]
    delta2 = track[:,1] - track[:,4]
    delta3 = track[:,2] - track[:,5]
    if np.average(delta1[-50:])<1e-4 and np.average(delta2[-50:])<1e-4 and np.average(delta3[-50:])<1e-4:
        new_df = pd.DataFrame({'p':[args[0]],'r':[args[1]],'b':[args[2]],'alpha_c':[alpha]})
        global df
        df = df.append(new_df)

num = 0

prb = []
for i in np.linspace(-100,100,200):
    prb.append([i,28,3])

for i in prb:
    for x in np.logspace(-2,2,100):
        alpha = x
        func1(i)
        num += 1
        print(num/3/2e4)

prb = []
for i in np.linspace(-100,100,200):
    prb.append([10,i,3])

for i in prb:
    for x in np.logspace(-2,2,100):
        alpha = x
        func1(i)
        num += 1
        print(num/3/2e4)

prb = []
for i in np.linspace(-100,100,200):
    prb.append([10,28,i])

for i in prb:
    for x in np.logspace(-2,2,100):
        alpha = x
        func1(i)
        num += 1
        print(num/3/2e4)

df.to_csv('test.csv')
