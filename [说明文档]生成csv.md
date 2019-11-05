```python
from scipy.integrate import odeint
import numpy as np
import pandas as pd
```



`df = pd.DataFrame(columns=['p','r','b','alphac_a','alphac_b'])`

| p              | r          | b          | alphac_a           | alphac_b           |
| -------------- | ---------- | ---------- | ------------------ | ------------------ |
| 方程第一个参数 | 第二个参数 | 第三个参数 | 正向开始不同步的值 | 负向开始不同步的值 |

`t = np.arange(0, 30, 0.01)`

时间间隔

```python
def abs_average(a):
    sum = 0
    for i in a:
        sum += np.abs(i)
    return sum/len(a)
```

$$
\sum_{1}^{len(a)}{|a|}
$$

```python
def lorenz(w,t,p,r,b,alpha):
    x1,x2,x3,y1,y2,y3 = w
    return np.array([-p*x1+p*x2, r*x1-x2-x1*x3, x1*x2-b*x3,\
                     -p*y1+p*x2*(1+alpha), r*y1-y2-y1*y3, y1*y2-b*y3])
```

$$
\left\{
\begin{array}{c}
\frac{dx_1}{dt}\quad=-px_1+px_2\\
\frac{dx_2}{dt}\quad=rx_1-x_2-x_1x_3\\
\frac{dx_3}{dt}\quad=x_1x_2-bx_3\\
\frac{dy_1}{dt}\quad=-py_1+px_2(1+\alpha)\\
\frac{dy_2}{dt}\quad=ry_1-y_2-y_1y_3\\
\frac{dy_3}{dt}\quad=y_1y_2-by_3
\end{array}
\right.
$$

```python
def find_alphac(args=[10,28,3], x0=[50.0,50.0,50.0], y0=[1.0,1.0,1.0])

alpha = 0.1
```

| 参数 | x的初值  | y的初值 | alpha的值 |
| ---- | -------- | ------- | --------- |
| p=10 | x_1=50.0 | y_1=1.0 | 0.1       |
| r=28 | x_2=50.0 | y_2=1.0 |           |
| c=3  | x_3=50.0 | y_3=1.0 |           |

```python
continue_times = 40
while True:
    if continue_times > 0:
        continue_times -= 1
    else:
        alphac_a = -10
        break
    #重复四十次操作
    #当操作运行40次后，仍然同步则记录-10作为导致不同步的alpha值，记为alpha_a
    track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], alpha))
    #解上述方程
    delta1 = track[:,0] - track[:,3] #x_1-y_1
    delta2 = track[:,1] - track[:,4] #x_2-y_2
    delta3 = track[:,2] - track[:,5] #x_3-y_3
    if abs_average(delta1[-50:])<10 and abs_average(delta2[-50:])<10 and abs_average(delta3[-50:])<10:
        alpha *= 1.5
        continue
    else:
        alphac_a = alpha
        break
    #验证趋向稳定的后50个值是否同步
    #同步的判断标准是差值是否小于十，小于10则同步，大于10则不同步
    #若同步，则将alpha扩大到原来的1.5倍，再次运算
    #若不同步输出，当前alpha记为alpha_a
```



`alpha = -0.1`

| 参数 | x的初值  | y的初值 | alpha的值 |
| ---- | -------- | ------- | --------- |
| p=10 | x_1=50.0 | y_1=1.0 | -0.1      |
| r=28 | x_2=50.0 | y_2=1.0 |           |
| c=3  | x_3=50.0 | y_3=1.0 |           |

```python
continue_times = 40
while True:
    if continue_times > 0:
        continue_times -= 1
    else:
        alphac_b = 10
        break
    #重复四十次操作
    #当操作运行40次后，仍然同步则记录-10作为导致不同步的alpha值，记为alpha_b
    track = odeint(lorenz,(x0[0],x0[1],x0[2],y0[0],y0[1],y0[2]),t,args=(args[0], args[1], args[2], alpha))
    #解上述方程
    delta1 = track[:,0] - track[:,3] #x_1-y_1
    delta2 = track[:,1] - track[:,4] #x_2-y_2
    delta3 = track[:,2] - track[:,5] #x_3-y_3
    if abs_average(delta1[-50:])<10 and abs_average(delta2[-50:])<10 and abs_average(delta3[-50:])<10:
        alpha *= 2
        continue
    else:
        alphac_b = alpha
        break
    #验证趋向稳定的后50个值是否同步
    #同步的判断标准是差值是否小于十，小于10则同步，大于10则不同步
    #若同步，则将alpha扩大到原来的2倍，再次运算
    #若不同步输出，当前alpha记为alpha_b
```

以上均是find_alpha的函数内容

以下是储存部分

```python
new_df = pd.DataFrame({'p':[args[0]],'r':[args[1]],'b':[args[2]],'alphac_a':[alphac_a],'alphac_b':[alphac_b]})
global df
df = df.append(new_df)
```

创建一个pd

| p              | r          | b          | alphac_a           | alphac_b           |
| -------------- | ---------- | ---------- | ------------------ | ------------------ |
| 方程第一个参数 | 第二个参数 | 第三个参数 | 正向开始不同步的值 | 负向开始不同步的值 |

`num = 0`

追踪完成百分比

```python
prb = []
for i in np.linspace(-100,40,140):
    prb.append([i,28,3])

for i in prb:
    find_alphac(i)
    #改变参量，遍历运行
    num += 1
    print(num/400)
```

```python
'''
prb = []
for i in np.linspace(0,90,100):
    prb.append([10,i,3])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/250)

prb = []
for i in np.linspace(-5,5,50):
    prb.append([10,28,i])

for i in prb:
    find_alphac(i)
    num += 1
    print(num/250)
'''
```

```python
df.to_csv('test.csv')
```

保存文件

