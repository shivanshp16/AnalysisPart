    # Importing the required libraries

import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.io as pio

    # Importing the dataset
data=pd.read_csv('Factors State Wise Data crm.csv', engine='python' ,encoding='utf-8')  

    #Making the Correlation Matrix for Simple Factors

data1=data.loc[:32,'Total GSDP':'Deathrate']
data1=data1.corr()

    #Plotting Heatmap for Correlation

fig=px.imshow(data1,
    color_continuous_scale=px.colors.sequential.RdBu,
    title='Correlation Between Different Factors')

fig.update_layout(font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':22
    })

pio.write_html(fig,file="Heatmap for Simple Factors.html",auto_open=True)

    #Making the Correlation Matrix for Agricultural Factors
'''
data_temp=data.loc[:,'Total GSDP':'Growth in GSDP']
data2=data.loc[:,'Percent of Land Irrigated':'Total Non Agricultral Land']
data2=data_temp.join(data2)
data2=data2.corr()
'''
    #Plotting Heatmap for Correlation
'''
fig=px.imshow(data2,
    color_continuous_scale=px.colors.sequential.RdBu,
    title='Correlation Between Different Factors (Agricultural)')

fig.update_layout(font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':22
    })

pio.write_html(fig,file="Heatmap for Agricultural Factors.html",auto_open=True)
'''
    # Now a Heatmap for HDI and Happiness index
    # Importing the dataset for HDI and Happiness index
data_h=pd.read_csv('Happiness.csv', engine='python' ,encoding='utf-8')  

    #Making the Correlation Matrix for Simple Factors


data_h=data_h.corr()

    #Plotting Heatmap for Correlation

fig=px.imshow(data_h,
    color_continuous_scale=px.colors.sequential.RdBu,
    title='How does these Factors affect the Happiness Index')

fig.update_layout(font_family='Times New Roman',
    font_size=15,
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':22
    })
fig.show()
#pio.write_html(fig,file="How does these Factors affect the Happiness Index.html",auto_open=True)
