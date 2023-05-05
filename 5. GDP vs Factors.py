    # Importing the required libraries

from re import template
import numpy as np 
import pandas as pd
import os
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

    # Importing the dataset 
data=pd.read_csv('Factors State Wise Data crm.csv', engine='python' ,encoding='utf-8')

    #Making a DataSet without Indian Total
data_edit=data.loc[:32]

    #Plotting Chart for Area Vs Total GSDP

fig= px.scatter(data_edit,
    x='Area',y='Total GSDP',
    hover_data=['States','Area','Total GSDP'],
    color_continuous_scale=px.colors.sequential.Aggrnyl,
    color='Total GSDP',
    size='Area',
    size_max=60,
    title='Effect of Area of the State on GSDP',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Effect of Area of the State on GSDP.html",auto_open=True)

    #Plotting Chart for Population Vs Total GSDP

fig= px.scatter(data_edit,
    x='Population',y='Total GSDP',
    hover_data=['States','Population','Total GSDP'],
    color_continuous_scale=px.colors.sequential.Bluered,
    color='Total GSDP',
    size='Population',
    size_max=60,
    title='Effect of Population of the State on GSDP',
    trendline='ols',
    template='plotly_dark',)
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

pio.write_html(fig,file="Effect of Population of the State on GSDP.html",auto_open=True)
'''
    #Plotting Chart for Lenght of coastline Vs Total GSDP
'''
data_t=data_edit.loc[2:]                                    #Removing Andngaman Nicobar as its an Island

fig= px.scatter(data_t,
    x='Length of Coastline',y='Total GSDP',
    hover_data=['States','Length of Coastline','Total GSDP'],
    color_continuous_scale=px.colors.sequential.Aggrnyl_r,
    color='Total GSDP',
    size='Length of Coastline',
    size_max=60,
    title='Effect of Length of Coastline on GSDP',
    trendline='ols',
    template='plotly_dark',)
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

pio.write_html(fig,file="Effect of Length of Coastline on GSDP.html",auto_open=True)

    #Plotting Chart for Birthrate vs GSDP per capita
'''
fig= px.scatter(data_edit,
    x='Birthrate',y='GSDP per Capita',
    hover_data=['States','Birthrate','GSDP per Capita'],
    color_continuous_scale=px.colors.sequential.Reds,
    color='Birthrate',
    size='GSDP per Capita',
    size_max=60,
    title='Effect of Birthrate on GSDP per Capita',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Effect of Birthrate on GSDP per Capita.html",auto_open=True)
'''
    #Plotting Chart for Literacy Rate vs GSDP per capita

fig= px.scatter(data_edit,
    x='Literacy Rate',y='GSDP per Capita',
    hover_data=['States','Literacy Rate','GSDP per Capita'],
    color_continuous_scale=px.colors.sequential.Greens,
    color='Literacy Rate',
    size='GSDP per Capita',
    size_max=60,
    title='Relation between Literacy Rate and GSDP per Capita',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Relation between Literacy Rate and GSDP per Capita.html",auto_open=True)

    #Plotting Chart for Infant Mortality Rate vs GSDP per capita
'''
fig= px.scatter(data_edit,
    x='GSDP per Capita',y='Infant Mortality Rate',
    hover_data=['States','Infant Mortality Rate','GSDP per Capita'],
    color_continuous_scale=px.colors.sequential.Bluered,
    color='Infant Mortality Rate',
    size='GSDP per Capita',
    size_max=60,
    title='Effect of GSDP per Capita on Infant Mortality Rate',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Effect of GSDP per Capita on Infant Mortality Rate.html",auto_open=True)
'''
    #Plotting Chart for Infant Mortality Rate vs Literacy rate
'''
fig= px.scatter(data_edit,
    x='Literacy Rate',y='Infant Mortality Rate',
    hover_data=['States','Literacy Rate','Infant Mortality Rate'],
    color_continuous_scale=px.colors.sequential.Bluered,
    color='Infant Mortality Rate',
    size='Literacy Rate',
    size_max=40,
    title='Effect of Literacy on Infant Mortality Rate',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Effect of Literacy on Infant Mortality Rate.html",auto_open=True)
'''
    #Plotting Chart for Literacy and Birthrate
'''
fig= px.scatter(data_edit,
    x='Birthrate',y='Literacy Rate',
    hover_data=['States','Literacy Rate','Birthrate'],
    color_continuous_scale=px.colors.sequential.Bluered_r,
    color='Literacy Rate',
    size='Literacy Rate',
    size_max=40,
    title='Effect of Literacy on Birthrate',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Effect of Literacy on Birthrate.html",auto_open=True)
'''
    #Plotting Chart for Literacy and HDI
'''
fig= px.scatter(data_edit,
    x='Literacy Rate',y='HDI',
    labels={'HDI':'Human Development Index'},
    hover_data=['States','Literacy Rate','HDI'],
    color_continuous_scale=px.colors.sequential.Aggrnyl,
    color='HDI',
    size='Literacy Rate',
    size_max=50,
    title='Relation between Literacy and Human Development Index',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Relation between Literacy and Human Development Index.html",auto_open=True)
'''
    #Plotting Chart for GSDP per Capita and HDI
'''
fig= px.scatter(data_edit,
    x='HDI',y='GSDP per Capita',
    labels={'HDI':'Human Development Index'},
    hover_data=['States','HDI','GSDP per Capita'],
    color_continuous_scale=px.colors.sequential.Greens,
    color='HDI',
    size='GSDP per Capita',
    size_max=60,
    title='Relation between Human Development Index and GSDP per Capita',
    trendline='ols',
    template='plotly_dark')
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

pio.write_html(fig,file="Relation between Human Development Index and GSDP per Capit.html",auto_open=True)
'''
