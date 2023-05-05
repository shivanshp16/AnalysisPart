    # Importing the required libraries

import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.io as pio

    #Importing the dataset 

data=pd.read_csv('Comparision over the years.csv', engine='python', encoding='utf-8')

    #Checking for missing data
'''
print(data.isnull().sum())
data.describe(include='all')
print(data.isnull().sum(axis=1))
'''
    #Displaying the table 
'''
data.isnull().sum(axis=0)
print(data[sorted(data.columns,reverse=False)])
'''
    #There are no missing value in our data 
    #This signifies that the data cleaning part is not needed here


    #Calculating average growth of states over the years
    #By 'moving average' as GSDP is a time series

m_avg=data.loc[10:,'Duration':]
m_avg=m_avg.iloc[:,1:].rolling(window=2).mean() #Calculating rolling average

    #Sorting Values and creating index

m_avg['Duration']=['2015-16','2016-17','2017-18','2018-19','2019-20']
m_avg=m_avg.iloc[1:]                                                  #Removing the 2015-16 Row as it's Nan
m_avg=m_avg.set_index('Duration',drop=True)
m_avg=m_avg.T                                                         #Transpose
m_avg['State']=m_avg.index                                            #Making a new Column "State" and droping value of index in it
m_avg=m_avg.sort_values(by='State')
m_avg['Index']=range(len(m_avg))
m_avg=m_avg.set_index('Index')
m_avg['Average']=m_avg.sum(axis=1)/4                                  #Average Growth over a period of 4 years

#print(m_avg.head(10))  


    #Transforming the Dataframe into a catagorical view to plot
    #We need 3 column - Duration , Rolling Average , State

gsdp=m_avg.append(m_avg.iloc[0:,1:],sort=False)
gsdp.loc[np.isnan(gsdp['2016-17']),['2016-17']]=m_avg['2017-18']
gsdp=gsdp.append(gsdp.iloc[0:,1:],sort=False)
gsdp.loc[np.isnan(gsdp['2016-17']),['2016-17']]=m_avg['2018-19']
gsdp=gsdp.append(gsdp.iloc[0:,1:],sort=False)
gsdp.loc[np.isnan(gsdp['2016-17']),['2016-17']]=m_avg['2019-20']
gsdp=gsdp.iloc[0:,[0,4,5]]

gsdp.columns=['Rolling Average','States','Average Growth']      #Renaming Columns
gsdp.drop_duplicates(subset=None,keep='first',inplace=True)     #Removing Duplicate Values

    #Updating the Durations

gsdp['Duration']=['2016-17' for i in range(len(gsdp))]  
gsdp.iloc[34:,3]='2017-18'
gsdp.iloc[68:,3]='2018-19'  
gsdp.iloc[102:,3]='2019-20'

gsdp['Rolling Average']=gsdp['Rolling Average'].apply(lambda x:round(x,2))     #Rounding the decimal Values to 2 places
gsdp.sort_values(by=['Average Growth','Duration',],ascending=[False,True],inplace=True) 

    #Dividing States based on National Average

gsdp['Index']=range(len(gsdp))
gsdp=gsdp.set_index('Index')
top=gsdp.loc[0:71]
bottom=gsdp.loc[68:]

    #Plotting for Top States 
    #Making Interactive Graph using plotly

fig= px.bar(top,
    x='States',y='Rolling Average',
    labels={'Rolling Average':'Growth(%)'},
    hover_data=['States','Duration','Rolling Average'],
    barmode='group',
    color='Duration',
    title='Average Growth of Top States')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="TopStates.html",auto_open=True)


    #Plotting for Bottom States 
    #Making Interactive Graph using plotly

fig= px.bar(bottom,
    x='States',y='Rolling Average',
    labels={'Rolling Average':'Growth(%)'},
    hover_data=['States','Duration','Rolling Average'],
    barmode='group',
    color='Duration',
    title='Average Growth of Bottom States')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="BottomStates.html",auto_open=True)

    
    #Ranking of States by Total GSDP in 2019-20
    #Sorting Values and making appropriate Table

state_gsdp=data.loc[7:7,'Andhra Pradesh':'Puducherry']
state_gsdp=state_gsdp.T                                 #Transpose
state_gsdp.columns=['GSDP']
state_gsdp['State']=state_gsdp.index
state_gsdp['GSDP']=state_gsdp['GSDP'].astype(float)     #Converting GSDP values into Float type
state_gsdp.sort_values(by=['GSDP'],ascending=[False],inplace=True) 

    #Plotting Chart

fig= px.bar(state_gsdp,
    x='State',y='GSDP',
    hover_data=['State','GSDP'],
    color='State',
    title='Ranking of States by Total GSDP in 2019-20')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Total GSDP in 2019-20.html",auto_open=True)


    #Ranking of States by GSDP Per Capita in 2019-20
    #Importing required CSV and sorting values

gsdp_pc=pd.read_csv('GDP per capita of States.csv', engine='python', encoding='utf-8')

    #Checking for missing data
'''
print(gsdp_pc.isnull().sum())
gsdp_pc.describe(include='all')
print(gsdp_pc.isnull().sum(axis=1))
'''
    #Displaying the table 
"""
data.isnull().sum(axis=0)
print(data[sorted(data.columns,reverse=False)])
"""
    #There are no missing value in our data 
    #This signifies that the data cleaning part is not needed here

    #Sorting Values 

gsdp_pc.sort_values(by=['GSDP per capita'],ascending=[False],inplace=True) 

    #Plotting Chart

fig= px.bar(gsdp_pc,
    x='States',y='GSDP per capita',
    labels={'States':'State'},
    hover_data=['States','GSDP per capita'],
    color='States',
    title='Ranking of States by GSDP Per Capita in 2019-20')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by GSDP Per Capita in 2019-20.html",auto_open=True)
