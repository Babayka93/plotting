unique_values = data['whoAmI'].unique()


for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

data = data.drop('whoAmI', axis=1)  

data.head()