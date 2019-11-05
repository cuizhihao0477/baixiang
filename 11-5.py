from scipy.integrate import odeint
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['p','r','b','alphac_a'])
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

def find_alphac(args=[10,28,3], x0=[1.0,1.0,1.0], y0=[100.0,100.0,100.0]):
    
    alpha = 1e-8
    continue_times = 100
    while True:
        if continue_times > 0:
            continue_times -= 1
        else:
            alphac_a = -10
            break
        track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], alpha))
        delta1 = track[:,0] - track[:,3]
        delta2 = track[:,1] - track[:,4]
        delta3 = track[:,2] - track[:,5]
        if abs_average(delta1[-100:])<1e-6 and abs_average(delta2[-100:])<1e-6 and abs_average(delta3[-100:])<1e-6:
            alpha += 1e-8
            continue
        else:
            alphac_a = alpha
            break
    '''
    alpha = -1e-7
    continue_times = 40
    while True:
        if continue_times > 0:
            continue_times -= 1
        else:
            alphac_b = 10
            break
        track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], alpha))
        delta1 = track[:,0] - track[:,3]
        delta2 = track[:,1] - track[:,4]
        delta3 = track[:,2] - track[:,5]
        if abs_average(delta1[-50:])<1e-6 and abs_average(delta2[-50:])<1e-6 and abs_average(delta3[-50:])<1e-6:
            alpha *= 2
            continue
        else:
            alphac_b = alpha
            break
    '''
    new_df = pd.DataFrame({'p':[args[0]],'r':[args[1]],'b':[args[2]],'alphac_a':[alphac_a]})
    global df
    df = df.append(new_df)

num = 0
'''
prb = []
for i in np.linspace(0,25,200):
    prb.append([i,28,3])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/400)
'''

prb = []
for i in np.linspace(0,100,1000):
    prb.append([10,i,3])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/1000)
'''
prb = []
for i in np.linspace(0,100,1000):
    prb.append([10,28,i])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/1000)
'''

df.to_csv('test.csv')
