# importing all the necesary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# importing the dataset(Data I-A)
# Dataset name: ab40c054-5031-4376-b52e-9813e776f65e.csv

df1=pd.read_csv('compare.csv',engine='python',encoding='utf-8')

# Index 5 and 10 having maximum numbers of null values.

df1.isnull().sum(axis=1)

# Removing the rows(Index 5 and 10): '(% Growth over the previous year)'
# and 'GSDP - CURRENT PRICES (` in Crore)' for the year 2016-17.

sf=pd.concat([df1[0:5],df1[6:10]],axis=0)
sf.isnull().sum(axis=1)

# Column "West Bengal1" is having null data

sf.isnull().sum(axis=0)
sf[sorted(sf.columns,reverse=True)]

# Removing the column="West Bengal1" as it has all null values

sf=sf.loc[:,~sf.columns.isin(["West Bengal1"])]
sf.isnull().sum(axis=1)

# Removing the columns(States) which having null values for 2015-16 

# As it is the best approach to get the data transformed without predicting any approximating values.

sf=sf.loc[:,~sf.columns.isin(["Himachal Pradesh",'Maharashtra','Manipur','Mizoram','Nagaland','Punjab','Rajasthan','Tripura','Andaman & Nicobar Islands'])]
sf.isnull().sum(axis=1)

# calculating the average growth of states over duartion 2012-13, 2013-14,2014-15 and 2015-16
# by "moving average"

m_avg=sf.loc[6:,'Duration':]

m_avg=m_avg.iloc[:,1:].rolling(window=2).mean() #rolling average calculating

# Making appropriate transformation like creating index and sorting the values

m_avg['Duration']=['2012-13','2013-14','2014-15','2015-16']
m_avg=m_avg.iloc[1:]
m_avg=m_avg.set_index('Duration',drop=True)
m_avg=m_avg.T
m_avg['Index']=range(len(m_avg))
m_avg['State']=m_avg.index
m_avg=m_avg.set_index('Index').sort_values(by='State')

print(m_avg.head(5))

# Transfoming the dataframe into a catagorial view to plot

gsdp=m_avg.append(m_avg.iloc[0:,1:],sort=False)
gsdp.loc[np.isnan(gsdp['2013-14']),['2013-14']]=m_avg['2014-15']
gsdp=gsdp.append(gsdp.iloc[0:,1:],sort=False)
gsdp.loc[np.isnan(gsdp['2013-14']),['2013-14']]=m_avg['2015-16']
gsdp=gsdp.iloc[0:,0::3]