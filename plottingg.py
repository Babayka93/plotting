import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем новые столбцы для каждого уникального значения
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[f'is_{value}'] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец, если нужно
data.drop(columns=['whoAmI'], inplace=True)

print(data.head())