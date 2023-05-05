# Importing the required libraries

import numpy as np 
import pandas as pd
import os
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

    #Taking All the Files in the current Directory
files = os.listdir(os.getcwd()) 
concated=[]
    #Sorting Files with gsva Data and Merging Them
for i in files:
    if i.find('.xlsx')>0:
        gsva=pd.read_csv(i,engine='python',encoding='ISO-8859-1')
        gsva['State']=i.split('.')[0]      #Making a State column and taking value from File Name
        concated.append(gsva)

gsva=pd.concat(concated,sort=False)
gsva_e=gsva[['Item','2019-20','State']]                       #Retaining only Selected Columns
gsva_e.sort_values(by='State',ascending=True,inplace=True)    #Sorting by State

    #Creating Index
gsva_e['Index']=range(len(gsva_e))
gsva_e.set_index('Index',inplace=True)

    #Removing Andaman & Nicobar and Chandigarh as their data is not Up-to-Date
gsva_e.drop(gsva_e[gsva_e['State']=='Andaman_Nicobar'].index, inplace=True)
gsva_e.drop(gsva_e[gsva_e['State']=='Chandigarh'].index, inplace=True)

    #Checking Data For Missing Values
'''
print(gsva_e.isnull().sum(axis=0))
'''
    #Removing Rows with null and zeros in them
    #Replacing 0's with Nan

gsva_e=gsva_e.replace(0,np.nan)

    #Finding out which rows have null values
'''
print(gsva_e[gsva_e.isnull().sum(axis=1)==1])
'''
    #Dropping the null value rows
gsva_e=gsva_e.drop(gsva_e[gsva_e.isnull().sum(axis=1)==1].index) 
'''
print(gsva_e.isnull().sum(axis=0))
'''

    #Making a Piechart showing Contribution of each Sector in GSDP
    #Seperating values of each sector 
'''
primary=gsva_e.loc[gsva_e['Item']=='Primary']
primary.sort_values(by='State')

secondary=gsva_e.loc[gsva_e['Item']=='Secondary']
secondary.sort_values(by='State')

tertiary=gsva_e.loc[gsva_e['Item']=='Tertiary']
tertiary.sort_values(by='State')

    #Separating GSDP by State
gross=gsva_e.loc[gsva_e['Item']=='Gross State Domestic Product']
gross.sort_values(by='State')

    #Calculating Contribution of each sector
primary_c=round(primary['2019-20'].sum()/gross['2019-20'].sum()*100,2)
secondary_c=round(secondary['2019-20'].sum()/gross['2019-20'].sum()*100,2)
tertiary_c=round(tertiary['2019-20'].sum()/gross['2019-20'].sum()*100,2)

    #Making a combined list for Plotting

contribution=[]
contribution.append(primary_c)
contribution.append(secondary_c)
contribution.append(tertiary_c)
contribution.append(round(100-sum(contribution),2))

print(contribution)
'''
    #Plotting a PieChart
'''
labels=['Primary','Secondary','Tertiary','Others']

colors = ['gold', 'yellowgreen', 'coral', 'skyblue']

fig=go.Figure(data=[go.Pie(labels=labels,values=contribution)])

fig.update_traces(
    hoverinfo='label+percent',textinfo='label+percent',
    textfont_size=15,
    marker=dict(colors=colors))

fig.update_layout(
    font_family='Times New Roman',
    title={
        'text':'Contribution of Sectors in GSDP',
        'y':0.92,
        'x':0.48,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':25
    })

pio.write_html(fig,file='PieChart - Contribution of Sectors in GSDP.html',auto_open=True)
'''
    #Preparing Data for Linechart
'''
gsva_s=gsva
gsva_s=gsva_s.drop(['S.No.','2020-21'],axis=1)
gsva_s.sort_values(by='State',ascending=True,inplace=True)    #Sorting by State

    #Creating Index
gsva_s['Index']=range(len(gsva_s))
gsva_s.set_index('Index',inplace=True)

    #Removing Andaman & Nicobar and Chandigarh as their data is not Up-to-Date
gsva_s.drop(gsva_s[gsva_s['State']=='Andaman_Nicobar'].index, inplace=True)
gsva_s.drop(gsva_s[gsva_s['State']=='Chandigarh'].index, inplace=True)

    #Retaining rows with Sector values
primary_s=gsva_s.loc[gsva_s['Item']=='Primary']
primary_s.sort_values(by='State')

secondary_s=gsva_s.loc[gsva_s['Item']=='Secondary']
secondary_s.sort_values(by='State')

tertiary_s=gsva_s.loc[gsva_s['Item']=='Tertiary']
tertiary_s.sort_values(by='State')

    #Adding Sum of Year wise Primary sector values 
y2011=round(primary_s['2011-12'].sum(),2)
y2012=round(primary_s['2012-13'].sum(),2)
y2013=round(primary_s['2013-14'].sum(),2)
y2014=round(primary_s['2014-15'].sum(),2)
y2015=round(primary_s['2015-16'].sum(),2)
y2016=round(primary_s['2016-17'].sum(),2)
y2017=round(primary_s['2017-18'].sum(),2)
y2018=round(primary_s['2018-19'].sum(),2)
y2019=round(primary_s['2019-20'].sum(),2)

pcontri=[y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019]

    #Adding Sum of Year wise Secondary sector values 
y2011=round(secondary_s['2011-12'].sum(),2)
y2012=round(secondary_s['2012-13'].sum(),2)
y2013=round(secondary_s['2013-14'].sum(),2)
y2014=round(secondary_s['2014-15'].sum(),2)
y2015=round(secondary_s['2015-16'].sum(),2)
y2016=round(secondary_s['2016-17'].sum(),2)
y2017=round(secondary_s['2017-18'].sum(),2)
y2018=round(secondary_s['2018-19'].sum(),2)
y2019=round(secondary_s['2019-20'].sum(),2)

scontri=[y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019]

    #Adding Sum of Year wise Tertiary sector values 
y2011=round(tertiary_s['2011-12'].sum(),2)
y2012=round(tertiary_s['2012-13'].sum(),2)
y2013=round(tertiary_s['2013-14'].sum(),2)
y2014=round(tertiary_s['2014-15'].sum(),2)
y2015=round(tertiary_s['2015-16'].sum(),2)
y2016=round(tertiary_s['2016-17'].sum(),2)
y2017=round(tertiary_s['2017-18'].sum(),2)
y2018=round(tertiary_s['2018-19'].sum(),2)
y2019=round(tertiary_s['2019-20'].sum(),2)

tcontri=[y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019]

year=['2011','2012','2013','2014','2015','2016','2017','2018','2019']
    #Plotting LineChart

fig=go.Figure()
fig.add_trace(go.Scatter(
    x=year,y=pcontri,
    mode='lines+markers',
        marker={'size':15},
    name='Primary',
        line=dict(color='green',width=3)
))
fig.add_trace(go.Scatter(
    x=year,y=scontri,
    mode='lines+markers',
        marker={'size':15},
    name='Secondary',
        line=dict(color='red',width=3)
))
fig.add_trace(go.Scatter(
    x=year,y=tcontri,
    mode='lines+markers',
        marker={'size':15},
    name='Tertiary',
        line=dict(color='royalblue',width=3)
))
fig.update_layout(
    template='plotly_dark',
    font_family='Times New Roman',
    font_size=15,
    xaxis_title='Years',
    yaxis_title='GDP Contributed (in Lakhs)',
    title={
        'text':'GDP Distribution of India over the Years',
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })
pio.write_html(fig,file="GDP Distribution of India over the Years.html",auto_open=True)
'''

    #Comparing Contribution of Sectors in different states
'''
array=['Maharashtra','Uttar Pradesh','Tamil Nadu','Karnataka','Gujarat',
    'West Bengal','Rajasthan','Andhra Pradesh','Telengana','Madhya Pradesh']
state_contri=gsva_e.loc[gsva_e['State'].isin(array)]
array1=['Primary','Secondary','Tertiary']
state_contri=state_contri.loc[state_contri['Item'].isin(array1)]

state_contri.sort_values(by=['State','Item'],ascending=[True,True],inplace=True)

final=pd.DataFrame(columns=['State','Primary','Secondary','Tertiary'])
for i in array:
    temp=state_contri.loc[state_contri['State']==i]
    total=temp['2019-20'].sum()
    primary=int(temp.iloc[0]['2019-20'])/int(total)*100
    secondary=int(temp.iloc[1]['2019-20'])/int(total)*100
    tertiary=int(temp.iloc[2]['2019-20'])/int(total)*100
    row={'State':i,'Primary':primary,'Secondary':secondary,'Tertiary':tertiary}
    final=final.append(row,ignore_index=True)

    #Plotting Stacked Bar Chart
fig=px.bar(final,
    x='State',y=['Primary','Secondary','Tertiary'],
    color_discrete_sequence=['green','red','royalblue'],
    title='Comparision of top 10 States by Sector Distribution',
    template='plotly_dark'
    )
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
pio.write_html(fig,file="Comparision of top 10 States by Sector Distribution.html",auto_open=True)
'''
#Comparing Contribution of Sectors in different states
array=['Maharashtra','Uttar Pradesh','Tamil Nadu','Karnataka','Gujarat',
    'West Bengal','Madhya Pradesh','Haryana','Goa','Sikkim']
state_contri=gsva_e.loc[gsva_e['State'].isin(array)]
array1=['Primary','Secondary','Tertiary']
state_contri=state_contri.loc[state_contri['Item'].isin(array1)]

state_contri.sort_values(by=['State','Item'],ascending=[True,True],inplace=True)

final=pd.DataFrame(columns=['State','Primary','Secondary','Tertiary'])
for i in array:
    temp=state_contri.loc[state_contri['State']==i]
    total=temp['2019-20'].sum()
    primary=int(temp.iloc[0]['2019-20'])/int(total)*100
    secondary=int(temp.iloc[1]['2019-20'])/int(total)*100
    tertiary=int(temp.iloc[2]['2019-20'])/int(total)*100
    row={'State':i,'Primary':primary,'Secondary':secondary,'Tertiary':tertiary}
    final=final.append(row,ignore_index=True)

    #Plotting Stacked Bar Chart
fig=px.bar(final,
    x='State',y=['Primary','Secondary','Tertiary'],
    color_discrete_sequence=['green','red','royalblue'],
    title='Comparision of States by Sector Distribution',
    template='plotly_dark'
    )
fig.update_layout(
    yaxis_title='Percent Contributed',
    font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })
 
pio.write_html(fig,file="Comparision of States by Sector Distribution.html",auto_open=True)