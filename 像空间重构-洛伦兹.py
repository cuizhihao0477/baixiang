from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def lorenz(w, t, p, r, b):
    x, y, z = w
    return np.array([p*(y-x), x*(r-z)-y, x*y-b*z])

t = np.arange(0, 100, 0.001)
track = odeint(lorenz, (20., 20., 40.), t, args=(10., 28., 8./3.))

'''
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track[:,0], track[:,1], track[:,2])
plt.show()
'''

z = track[:,2]
list = []
n = len(z)
for i in range(n):
    if i == 0 or i == n-1:
        continue
    if z[i]>z[i-1] and z[i]<z[i+1]:
        list.append(z[i])
x = []
y = []
for i in range(len(list)):
    if i == 0:
        continue
    if np.abs(list[i]-list[i-1])<1:
        continue
    x.append(list[i-1])
    y.append(list[i])

plt.plot(x,y,'.')
plt.show()
