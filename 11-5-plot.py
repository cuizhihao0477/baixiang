import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\ruirui_feng\Desktop\百项\02\test2.csv')

font = {'family' : 'simhei',
        'weight' : 'regular',
        'size'   : '15'}
plt.rc('font', **font)
plt.rcParams['axes.unicode_minus']=False

p = []
p_alpha = []
r = []
r_alpha = []
b = []
b_alpha = []

for i in range(800):
    x = df.iloc[i,:]
    if x['r']==28 and x['b']==3:
        p.append(x['p'])
        p_alpha.append(x['alphac_a'])
    elif x['p']==10 and x['b']==3:
        r.append(x['r'])
        r_alpha.append(x['alphac_a'])
    else:
        b.append(x['b'])
        b_alpha.append(x['alphac_a'])

plt.plot(p,p_alpha)
plt.xlabel(r'$p$')
plt.ylabel(r'$\alpha_c$')
plt.title('抗噪曲线($\Delta=10^{-6}$)')
plt.show()
