import pandas as pd
df = pd.read_csv('test.csv')

p = []
p_alpha = []
r = []
r_alpha = []
b = []
b_alpha = []

for i in range(20468):
    x = df.iloc[i,:]
    if x['r']==28 and x['b']==3:
        p.append(x['p'])
        p_alpha.append(x['alpha_c'])
    elif x['p']==10 and x['b']==3:
        r.append(x['r'])
        r_alpha.append(x['alpha_c'])
    else:
        b.append(x['b'])
        b_alpha.append(x['alpha_c'])

import matplotlib.pyplot as plt
plt.subplot(1,3,1)
plt.xlim([-100,100])
plt.plot(p,p_alpha)
plt.subplot(1,3,2)
plt.xlim([-100,100])
plt.plot(r,r_alpha)
plt.subplot(1,3,3)
plt.xlim([-100,100])
plt.plot(b,b_alpha)
plt.show()
