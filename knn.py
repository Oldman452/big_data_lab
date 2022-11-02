
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
import openpyxl

df = pd.read_excel('dataset.xlsx')

dict_decode = {0:'чай',1:'кофе'}
df['К/Ч'] = df['К/Ч'].replace({'ч':0,'к':1})
df['мама'] = df.iloc[:,5].map(lambda x:x[0]).replace({'ч':0,'к':1})
df['папа'] = df.iloc[:,5].map(lambda x:x[1]).replace({'ч':0,'к':1})
df = df.drop(columns=['Родители (мама, папа) что пьют'])
df.head()

train_idx = np.random.choice(np.arange(19),size = 17,replace=False)
test_idx = list(set(np.arange(19))  - set(train_idx))
train = df.iloc[train_idx]
test = df.iloc[test_idx]


def search_drink_knn(train_df, new_object, k=5, type_norm=2):
    help_dict = {0: 'Чай', 1: 'Кофе'}
    train_df['close_neighbor'] = (np.linalg.norm(train_df.drop(columns=['К/Ч']) - new_object,ord=type_norm, axis=1))
    answer = train_df.sort_values('close_neighbor').iloc[:k]['К/Ч'].value_counts().index.tolist()[0]
    return f'Человек с этими параметрами пьет: {help_dict[answer]}'


time_sleep = int(input('Часы сна:'))
work = int(input('Трудоустройство:'))
weight = int(input('Вес:'))
height = int(input('Рост:'))
distance = float(input('Расстояние до МИРЭА в часах:'))
mom = input('Что пьет мама:')
dad = input('Что пьет папа:')
dict_encode = {'чай':0,'кофе':1}
input_data = np.array([time_sleep, work, weight ,height, distance, dict_encode[mom.lower()], dict_encode[dad.lower()]])


print(search_drink_knn(df,input_data))
print('Самое близкое расстояние',sorted(df.close_neighbor)[0])
print(df.sort_values(by='close_neighbor'))

print(search_drink_knn(train,test.iloc[0,[0,1,2,3,4,6,7]]))
print('Указанное предпочтение',dict_decode[test.iloc[0,5]])

sns.set_theme()
sns.pairplot(data = df, hue = 'К/Ч')
