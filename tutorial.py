import seaborn as sns
import pandas as pd

# what is a dataframe

# load data
data = sns.load_dataset('iris')
df = pd.DataFrame(data)

# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')

# import sqlite3
# conn = sqlite.connect('database.db')
# df = pd.read_sql(query, conn)

# df = pd.read_json('data.json')

# exploring data
# print(df.head(10))
# print(df.tail())
# print(df.shape)
# print(df.dtypes)
# print(df.describe())

# print(df.head())
# sorted_df = df.sort_values(['sepal_length', 'petal_width'], ascending=False)
# print(sorted_df.head())

# print(df.head())
# del df['species']
# grouped_df = df.groupby('petal_length').mean()
# # sum(), count(), etc.
# print(grouped_df)

# filtered_df = df[(df['petal_length'] > 1.3)]
# print(filtered_df.head())

# data manipulation

# column = df['petal_width']
# print(column)

# columns = df[['petal_width', 'petal_length']]
# print(columns)

# grouped_data = df.groupby('petal_width').agg({'petal_width': 'count'})
# print(grouped_data)

"""
Questions to answer
1. difference between average max temperature per day and record max temp per day
2. Sort hottest months of the year by max avg temp
https://github.com/fivethirtyeight/data/blob/master/us-weather-history/KCLT.csv
"""

# 1.
# read csv data
df = pd.read_csv('data.csv')
# create a new column and subtract record from average
df['max_temp_difference'] = df['record_max_temp'] - df['average_max_temp']
# print out sorted df ascending = False
# print(df.sort_values('max_temp_difference', ascending=False))

# 2.
# setup date time column
df['date'] = pd.to_datetime(df['date'], format='ISO8601')
# group by data (month) with the max average_max_temp value
date_grouped_df = df.groupby(df.date.dt.month)['average_max_temp'].max()
# sort data
max_temp_sorted = date_grouped_df.sort_values(ascending=False)
# print
print(max_temp_sorted)
