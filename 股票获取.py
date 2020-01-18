# -*- coding: utf-8 -*
from pandas_datareader import data,wb
from datetime import datetime
import matplotlib.pyplot as plt

end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)

gold = data.DataReader('Gold' , 'yahoo' ,start,end)
silver = data.DataReader('SIL' , 'yahoo' , start,end)
gold = gold['Adj Close']
gold.name = 'gold'
silver = silver['Adj Close']
silver.name = 'silver'

gold.plot(legend=True,figsize=(10,4))
silver.plot(legend=True,figsize=(10,4))
plt.show()


























































