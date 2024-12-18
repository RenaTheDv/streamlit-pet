import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
зш
#Код sidebar'a
st.sidebar.title('Доступные страницы:')
st.sidebar.write('__MAIN__ - основная страница с информацией про компанию Apple...')
st.sidebar.write('__TIPS__ - страница с графиком по DataFrame, связанным с исследованием по чаевым...')
st.sidebar.write('__PLOT__ - страница с возможность загрузить ваш DataFrame и построить по нему графики...')

#Дадим выбор из четырех графиков для построения...
#Для каждого графика добавим возможность выбора hue параметра (если применимо?)

st.title('Визуализация вашего CSV')

uploaded_file = st.file_uploader('Выберите ваш CSV', type='csv')

#Добавим рандомные HEX для вывода графика в цвете (рандомном)
random_color = ['#d10d0d','#ebd61c','#2ec953','#2ec7c9','#182fad','#681cba','#b51cba','#ba1c51','#d45f24','#237dc2']

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('DataFrame (первые 10 строк):')
    st.write(df.head(10))

    #Выбираем колонки для построения графика
    x_col = st.selectbox('Выберите col для X-оси:', df.columns)
    y_col = st.selectbox('Выберите col для Y-оси:', df.columns)
    hue = st.selectbox('Выберите col для использования в hue (если применимо)', ['Нет'] + list(df.columns))

    #Пропишем условие, если хотят построить график с hue, а оно не выбрано:
    if hue == 'Нет':
        hue = None

    #Пусть строится график с hue и без него, кнопки рядом!
    sc_col1, sc_col2 = st.columns(2)

#Строим scatterplot для выбранных колонок и с выбранным режими...
    with sc_col1:
        if st.button('Построй мне **scatterplot** без зависимости!'):
            st.write(f'Scatterplot: {x_col}, {y_col}')

            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x=x_col, y=y_col, label=f'{x_col} vs {y_col}', color=random.choice(random_color), alpha=0.7, s=100, ax=ax)
            plt.xticks(rotation=45)
            plt.yticks(rotation=30)
            plt.title(f'Scatterplot: col {x_col} vs col {y_col}.')
            plt.legend()
            st.pyplot(fig)

    with sc_col2:
        if st.button('Построй мне **scatterplot** c зависимостью!'):
            if hue == None:
                st.write('Аргумент **hue** не выбран.')
            else:
                st.write(f'Scatterplot: {x_col}, {y_col}, {hue}')

                fig, ax = plt.subplots()
                sns.scatterplot(data=df, x=x_col, y=y_col,hue=hue, palette=random_color, alpha=0.7, s=100, ax=ax)
                plt.xticks(rotation=45)
                plt.yticks(rotation=30)
                plt.title(f'Scatterplot: col {x_col} vs col {y_col}.')
                plt.legend()
                st.pyplot(fig)

#Строим lineplot 
    lp_col1, lp_col2 = st.columns(2)
    with lp_col1:
        if st.button('Построй мне **lineplot** без зависимостей!'):
            st.write(f'Lineplot: {x_col}, {y_col}')

            fig, ax = plt.subplots()
            sns.lineplot(data=df, x=x_col, y=y_col, label=f'{x_col} vs {y_col}', color=random.choice(random_color), linewidth=6, ax=ax)
            plt.xticks(rotation=45)
            plt.yticks(rotation=30)
            st.pyplot(fig)

    with lp_col2:
        if st.button('Построй мне **lineplot** с зависимостью!'):
            if hue == None:
                st.write('Аргумент **hue** не выбран.')
            else:
                st.write(f'Lineplot: {x_col}, {y_col}, {hue}.')

                fig, ax = plt.subplots()
                sns.lineplot(data=df, x=x_col, y=y_col, hue=hue, palette=random_color, linewidth=6, ax=ax)
                plt.xticks(rotation=45)
                plt.yticks(rotation=30)
                st.pyplot(fig)

#Строим histplot
    hp_col1, hp_col2 = st.columns(2)

    with hp_col1:
        if st.button('Построй мне **histplot** без зависимостей!'):
            st.write(f'Histplot: {x_col}.')

            fig, ax = plt.subplots()
            sns.histplot(data=df, x=x_col, ax=ax, kde=True, label=f'col {x_col}', color=random.choice(random_color))
            plt.xticks(rotation=45)
            plt.yticks(rotation=30)
            plt.legend()
            st.pyplot(fig)

    with hp_col2:
        if st.button('Построй мне **histplot** с зависимостью!'):
            if hue ==  None:
                st.write('Аргумент **hue** не выбран.')
            else:
                st.write(f'Histplot: {x_col}, {hue}.')

                fig, ax = plt.subplots()
                sns.histplot(data=df, x=x_col, kde=True, hue=hue, palette=random_color, ax=ax)
                plt.xticks(rotation=45)
                plt.yticks(rotation=30)
                st.pyplot(fig)

#Строим boxplot
    bx_col1, bx_col2 = st.columns(2)

    with bx_col1:
        if st.button('Построй мне **boxplot** без зависимостей!'):
            st.write(f'Boxplot: {x_col}, {y_col}.')

            fig, ax = plt.subplots()
            sns.boxplot(data=df, x=x_col, y=y_col, label=f'col {x_col} vs {y_col}', color=random.choice(random_color), ax=ax)
            plt.xticks(rotation=45)
            plt.yticks(rotation=30)
            plt.legend()
            st.pyplot(fig)

    with bx_col2:
        if st.button('Построй мне **boxplot** с зависимостью!'):
            if hue == None:
                st.write('Аргумент **hue** не выбран.')
            else:
                st.write(f'Boxplot: {x_col}, {y_col}, {hue}.')

                fig, ax = plt.subplots()
                sns.boxplot(data=df, x=x_col, y=y_col, hue=hue, palette=random_color, ax=ax)
                plt.xticks(rotation=45)
                plt.yticks(rotation=30)
                st.pyplot(fig)

st.write('### Спасибо за тест!')


    

