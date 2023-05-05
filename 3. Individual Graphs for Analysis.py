    #In this file we are going to make State Wise Ranking Charts for 
'''
    Area , Population , Population Density , Coastline Length , Infant Mortality Rate ,
    Birthrate , Deathrate , Literacy    
'''
    # Importing the required libraries

import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.io as pio
'''
    # Importing the dataset 
data=pd.read_csv('Factors State Wise Data.csv', engine='python' ,encoding='utf-8')

    #Making a DataSet without Indian Total
data_edit=data.loc[:32]

    #Plotting Chart for Area

fig= px.bar(data_edit,
    x='States',y='Area (sq. km)',
    labels={'States':'State'},
    hover_data=['States','Area (sq. km)'],
    color='States',
    title='Ranking of States by Area')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Area.html",auto_open=True)

    #Plotting Chart for Population

fig= px.bar(data_edit,
    x='States',y='Population',
    labels={'States':'State'},
    hover_data=['States','Population'],
    color='States',
    title='Ranking of States by Population')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Population.html",auto_open=True)

    #Plotting Chart for Population Density

fig= px.bar(data,
    x='States',y='Pop. Density (per sq. km)',
    labels={'States':'State','Pop. Density (per sq. km)':'Population Density'},
    hover_data=['States','Pop. Density (per sq. km)'],
    color='States',
    title='Ranking of States by Population Density')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Population Density.html",auto_open=True)

    #Plotting Chart for Infant Mortality Rate

fig= px.bar(data,
    x='States',y='Infant mortality (per 1000 births)',
    labels={'States':'State','Infant mortality (per 1000 births)':'Infant Mortality Rate (per 1000 births)'},
    hover_data=['States','Infant mortality (per 1000 births)'],
    color='States',
    title='Ranking of States by Infant Mortality Rate')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Infant Mortality Rate.html",auto_open=True)

    #Plotting Chart for Birthrate

fig= px.bar(data,
    x='States',y='Birthrate',
    labels={'States':'State'},
    hover_data=['States','Birthrate'],
    color='States',
    title='Ranking of States by Birthrate')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Birthrate.html",auto_open=True)

    #Plotting Chart for Birthrate

fig= px.bar(data,
    x='States',y='Deathrate',
    labels={'States':'State'},
    hover_data=['States','Deathrate'],
    color='States',
    title='Ranking of States by Deathrate')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Deathrate.html",auto_open=True)

    #Plotting Chart for Literacy Rate

fig= px.bar(data,
    x='States',y='Literacy (%)',
    labels={'States':'State','Literacy (%)':'Literacy Rate'},
    hover_data=['States','Literacy (%)'],
    color='States',
    title='Ranking of States by Literacy Rate')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Literacy Rate.html",auto_open=True)

    #Making appropriate tranformations for Coastline Length

data_edit2=data_edit[['States','Coastline (coast/area ratio)']]
data_edit2=data_edit2.dropna()

    #Plotting Chart for Coastline Length

fig= px.bar(data_edit2,
    x='States',y='Coastline (coast/area ratio)',
    labels={'States':'State','Coastline (coast/area ratio)':'Coastline Length'},
    hover_data=['States','Coastline (coast/area ratio)'],
    color='States',
    title='Ranking of States by Length of Coastline')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Length of Coastline.html",auto_open=True)
'''
    # Importing the dataset 
data_h=pd.read_csv('Happiness.csv', engine='python' ,encoding='utf-8')

    #Plotting Chart for HDI

fig= px.bar(data_h,
    x='States',y='HDI',
    labels={'States':'State','HDI':'Human Development Index'},
    hover_data=['States','HDI'],
    color='States',
    title='Ranking of States by Human Development Index')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Human Development Index.html",auto_open=True)

    #Plotting Chart for Happiness Index

fig= px.bar(data_h,
    x='States',y='Happiness Index',
    labels={'States':'State','Happiness Index':'Happiness Rating'},
    hover_data=['States','Happiness Index'],
    color='States',
    title='Ranking of States by Happiness Rating')
fig.update_layout(
    font_family='Times New Roman',
    font_size=15,
    xaxis={'categoryorder':'total descending'},
    title={
        'y':0.94,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top',
        'font_size':23
    })

pio.write_html(fig,file="Ranking of States by Happiness Rating.html",auto_open=True)