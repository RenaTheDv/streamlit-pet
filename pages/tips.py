import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io

#Код sidebar'a
st.sidebar.title('Доступные страницы:')
st.sidebar.write('__MAIN__ - основная страница с информацией про компанию Apple...')
st.sidebar.write('__TIPS__ - страница с графиком по DataFrame, связанным с исследованием по чаевым...')

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

#Выведем df для наглядности
st.write('## DataFrame Tips')
st.write(tips)

#Задание 1
#Работа с df = tips
random_dates = pd.date_range(start=pd.to_datetime('2023-01-01'), end=pd.to_datetime('2023-01-31')).to_pydatetime().tolist()
tips['time_order'] = np.random.choice(random_dates, size=244)
tips.sort_values('time_order', inplace=True)

#Построение графика
fig1, ax1 = plt.subplots()
sns.lineplot(data=tips, x='time_order', y='tip', label='Tips', color='#1d10ad', ax=ax1)
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Tips', fontsize=12)
plt.title('Tips over time')

#Выгрузка графика на страницу streamlit
st.write('#### Динамика чаевых по времени...')
st.write('Использование метода **lineplot**.')
st.pyplot(fig1)

#Кнопка для скачивания
plt.savefig('lineplot1.png')
with open('lineplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='lineplot1.png',
        mime='image/png',
        key=1)

#Строим этот же график по-другому...
g = sns.relplot(data=tips, x='time_order', y='tip', kind='line', height=4, aspect=1.5, label='Tips')
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)                          #не получилось цвет поменять как на первом графике
plt.xlabel('Time', fontsize=12)
plt.ylabel('Tips', fontsize=12)
plt.legend()
plt.title('Tips over time')

st.write('Использование метода **relplot**.')
st.pyplot(g)

#Кнопка для скачивания
plt.savefig('lineplot2.png')
with open('lineplot2.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='lineplot2.png',
        mime='image/png',
        key=2)

#Задание 2
#Строим гистограмму total_bill
fig2, ax2 = plt.subplots()
sns.histplot(data=tips, x='total_bill', bins=20, label='Total bill', ax=ax2)
plt.legend()

#Выгрузка на страницу streamlit
st.write('#### Столбец total_bill через график-гистограмму и не только...')
st.write('Использование метода **histplot**.')
st.pyplot(fig2)

#Кнопка для скачивания
plt.savefig('histplot1.png')
with open('histplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='histplot1.png',
        mime='image/png',
        key=3)

#Строим этот же график по другому...
d = sns.displot(data=tips, x='total_bill', kind='hist', bins=20, height=4, aspect=1.5, label='Total bill')
plt.legend()

#Выгрузка на страницу streamlit
st.write('Использование метода **displot** (kind="hist").')
st.pyplot(d)

#Кнопка для скачивания
plt.savefig('displot1.png')
with open('displot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='displot1.png',
        mime='image/png',
        key=4)

#Играем с kind, строим новые графики
kde = sns.displot(data=tips, x='total_bill', kind='kde', height=4, aspect=1.5, label='Total bill')
plt.legend()

st.write('Поиграем с kind! Здесь kind="kde".')
st.pyplot(kde)

#Кнопка для скачивания
plt.savefig('displot2.png')
with open('displot2.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='displot1.png',
        mime='image/png',
        key=5)

ecdf = sns.displot(data=tips, x='total_bill', kind='ecdf', height=4, aspect=1.5, label='Total bill')
plt.legend()

st.write('Еще немного игр.... Здесь kind="ecdf".')
st.pyplot(ecdf)

#Кнопка для скачивания
plt.savefig('displot3.png')
with open('displot3.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='displot3.png',
        mime='image/png',
        key=6)

#Задание 3
#Строим scatterplot, связывая total_bill и tip
fig3, ax3 = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', palette='Set2', ax=ax3)

#Выгрузка на страницу streamlit
st.write('#### Свяжем признаки total_bill и tip, обозначив пол...')
st.write('Использования метода **scatterplot**.')
st.pyplot(fig3)

#Кнопка для скачивания
plt.savefig('scatterplot1.png')
with open('scatterplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='scatterplot1.png',
        mime='image/png',
        key=7)

#Строим этот же график по другому
rel = sns.relplot(data=tips, x='total_bill', y='tip', hue='sex', kind='scatter', palette='Set2', height=4, aspect=1.5)
rel._legend.remove()
rel.ax.legend(edgecolor='black', title='sex')

#Выгрузка на страницу streamlit
st.write('Использование метода **relplot**.')
st.pyplot(rel)

#Кнопка для скачивания
plt.savefig('relplot1.png')
with open('relplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='relplot1.png',
        mime='image/png',
        key=8)

#Задание 4
#Свяжем total_bill, tip и size на одном графике
fig4, ax4 = plt.subplots(figsize=(12, 7), dpi=80)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size', palette='Set1', s=70, ax=ax4)
plt.xlabel('Total bill', fontsize=13)
plt.ylabel('Tip', fontsize=13)
plt.legend(title='SIZE', ncol=3)

#Выгрузка на страницу streamlit
st.write('#### Свяжем признаки total_bill, tip и size...')
st.write('Использование метода **scatterplot**.')
st.pyplot(fig4)

#Кнопка для скачивания
plt.savefig('scatterplot2.png')
with open('scatterplot2.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='scatterplot2.png',
        mime='image/png',
        key=9)

#Задание 5
#Есть ли связь между днем недели и размером счета?
fig5, ax5 = plt.subplots()
sns.barplot(data=tips, x='day', y='total_bill', color='#0fafb8', label='Total bill', ax=ax5)
plt.yticks(range(0, 51, 10))
plt.xlabel('Days', fontsize=13)
plt.ylabel('Total bill', fontsize=13)
plt.title('Days and total bill')
plt.legend()

#Выгрузка на страницу streamlit
st.write('#### Найдем связь между day и total_bill...')
st.write('Использование метода **barplot**.')
st.pyplot(fig5)

#Кнопка для скачивания
plt.savefig('barplot1.png')
with open('barplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='barplot1.png',
        mime='image/png',
        key=10)

#Задание 6
#Нарисовать scatterplot - day по оси Y, tips по оси Х, цвет зависит от sex
for_palette = ['#3061c9', '#c9308f']
fig6, ax6 = plt.subplots(figsize=(12, 8), dpi=80)
sns.scatterplot(data=tips, x='tip', y='day', hue='sex', palette=for_palette, ax=ax6)
plt.xlabel('TIPS', fontsize=13)
plt.ylabel('DAYS', fontsize=13) 

#Выгрузка на страницу streamlit
st.write('#### Рисуем график с признаками day, tips, sex...')
st.write('Использование метода **scatterplot**.')
st.pyplot(fig6)

#Кнопка для скачивания
plt.savefig('scatterplot3.png')
with open('scatterplot3.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='scatterplot3.png',
        mime='image/png',
        key=11)

#Задание 7
#Рисуем boxplot с суммой всех счетов каждый день, разбивая по time
df = tips.groupby(['time_order', 'time'])['total_bill'].sum().reset_index(name='amount')

fig7, ax7 = plt.subplots()
sns.boxplot(data=df, x='time', y='amount', color='#c93b30', label='amount', ax=ax7)
plt.yticks(rotation=45)
plt.xlabel('Lunch or Dinner', fontsize=13)
plt.ylabel('Amount per day')
plt.title('Amount by time')
plt.legend()

#Выгружаем на страницу streamlit
st.write('#### Построим график с суммой всех счетов под дням amount, разбивая по time...')
st.write('Использование метода **boxplot**.')
st.pyplot(fig7)

#Кнопка для скачивания
plt.savefig('boxplot1.png')
with open('boxplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='boxplot1.png',
        mime='image/png',
        key=12)

#Строим такой же график, используя другой метод
df['color'] = 1

box = sns.catplot(data=df, x='time', y='amount', kind='box', hue='color', palette=['#c93b30'], height=4, aspect=1.5)
box._legend.remove()
box.ax.legend(edgecolor='black', title='amount')
plt.yticks(rotation=45)
plt.xlabel('Lunch or Dinner', fontsize=13)
plt.ylabel('Amount per day')
plt.title('Amount by time')

#Выгружаем на страницу streamlit
st.write('Использование метода **catplot**.')
st.pyplot(box)

#Кнопка для скачивания
plt.savefig('catplot1.png')
with open('catplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='catplot1.png',
        mime='image/png',
        key=13)

#Задание 8
#Рисуем две гистограммы чаевых на обед и ланч. Располагаем рядом
h = sns.displot(data=df, x='amount', col='time', kind='hist', bins=10, hue='color', palette=['#8e30c9'], kde=True, height=4, aspect=1.5)
for ax in h.axes.flat:
    ax.set_xlabel('TOTAL TIPS', fontsize=13, fontweight='bold')
    ax.set_ylabel('COUNT OF TIMES', fontsize=13, fontweight='bold')
h._legend.set_bbox_to_anchor((0.14, 0.87))
h._legend.set_title('tips for d + l')
plt.suptitle('Tips for dinner and lunch', fontsize=15)

#Выгружаем на страницу streamlit
st.write('#### Два графика чаевых на обед и ланч...')
st.write('Использование метода **displot** совместно с **hist**.')
st.pyplot(h)

#Кнопка для скачивания
plt.savefig('displot4.png')
with open('displot4.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='displot4.png',
        mime='image/png',
        key=14)

#Задание 9
#Два графика scatterplot (для мужчин и для женщин), связь размера чаевых и общей суммы за заказ (разбить по некурящим допольнительно)
df2 = tips.groupby(['sex', 'smoker', 'time_order'])[['total_bill', 'tip']].sum()
s = sns.relplot(data=df2, x='total_bill', y='tip', col='sex', kind='scatter', hue='smoker', palette='Set1', height=4, aspect=1.5)
for ax in s.axes.flat:
    ax.set_xlabel('TOTAL BILL', fontsize=12, fontweight='bold')
    ax.set_ylabel('TIP', fontsize=12, fontweight='bold')
s._legend.set_bbox_to_anchor((0.14, 0.87))
s._legend.set_title('smoker?')
s._legend.set_frame_on(True)
plt.suptitle('Tip and total bill', fontsize=15)

#Выгружаем на страницу streamlit
st.write('#### Свяжем tip, total_bill, разобьем по sex и smoker...')
st.write('Использование метода **relplot**.')
st.pyplot(s)

#Кнопка для скачивания
plt.savefig('scatterplot4.png')
with open('scatterplot4.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='scatterplot4.png',
        mime='image/png',
        key=15)

#Задание 10
#Тепловая зависимость числовых переменных
corr_matrix = tips.corr(numeric_only=True)

fig8, ax8 = plt.subplots(figsize=(10, 5))
# plt.figure(figsize=(10, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax8)

#Выгружаем на страницу streamlit
st.write('#### Тепловая зависимость числовых признаков...')
st.write('Использование метода **heatmap**.')
st.pyplot(fig8)

#Кнопка для скачивания
plt.savefig('heatmap1.png')
with open('heatmap1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='heatmap1.png',
        mime='image/png',
        key=16)

#Задание 11
#Изучаем pairplot с помощью tips
tips_to_num = tips.select_dtypes(include='number')

pa = sns.pairplot(data=tips_to_num, diag_kind='kde', markers='o')

#Выгружаем на страницу streamlit
st.write('#### Изучаем график pairplot на примере tips...')
st.write('Использование метода **pairplot**.')
st.pyplot(pa)

#Кнопка для скачивания
plt.savefig('pairplot1.png')
with open('pairplot1.png', 'rb') as img:
    st.download_button(
        label='Скачать этот график :arrow_up:',
        data=img,
        file_name='pairplot1.png',
        mime='image/png',
        key=17)

#Оформление конца страницы
st.write('### Kонец иследования... Спасибо за уделенное время! :milky_way:')