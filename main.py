import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf 

#Код для общего названия страницы
st.set_page_config(page_title='MultiApp')
#Код sidebat'a
st.sidebar.title('Доступные страницы:')
st.sidebar.write('__MAIN__ - основная страница с информацией про компанию Apple...')
st.sidebar.write('__TIPS__ - страница с графиком по DataFrame, связанным с исследованием по чаевым...')
st.sidebar.write('__PLOT__ - страница с возможность загрузить ваш DataFrame и построить по нему графики...')
#Название сайта
st.title('Simple App About Quotes :fire:')
#Описание работы сайта
st.write('Shows **closing price** and **volume** of Apple Company!')
#Сбор данных о котировках Apple в период с 01.01.2014 по 01.01.2024
ticker_symbol = 'AAPL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2014-1-1', end='2024-1-1')
#Построения графиков на основе данных
st.write("""
## Close price
""")
st.line_chart(ticker_df.Close, color='#7932a8')
st.write("""
## Volume price
""")
st.line_chart(ticker_df.Volume, color='#32a875')
