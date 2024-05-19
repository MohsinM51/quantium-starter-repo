import pandas as pd
import csv

data0 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_0.csv')
data1 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_1.csv')
data2 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_2.csv')
merged_data = pd.read_csv('/data filter/merged_data.csv')
product_pink_morsels = pd.read_csv('/data filter/product_pink_morsels.csv')
pink_morsel_data = pd.read_csv('/dash app for analysis/pink_morsel_data.csv')

# product_pink_morsels["price"] = product_pink_morsels["price"].str[1:]     deletes dollar sign from price
# print(product_pink_morsels.head())
# product_pink_morsels["price"] = product_pink_morsels["price"].astype(float)   converts price to float
# product_pink_morsels['sales'] = product_pink_morsels['price'] * product_pink_morsels['quantity']      creates sales column
# print(product_pink_morsels.head())
#
# product_pink_morsels=product_pink_morsels.to_csv("product_pink_morsels.csv")

# del product_pink_morsels["Unnamed: 0.1"]      experimenting
# del product_pink_morsels["Unnamed: 0"]
# print(product_pink_morsels)
# product_pink_morsels= product_pink_morsels[['sales','date','region']]
# product_pink_morsels.to_csv('product_pink_morsels.csv')
#
# print(product_pink_morsels.head())

# product_pink_morsels = product_pink_morsels[['sales','date','region']]
# product_pink_morsels.to_csv('product_pink_morsels.csv',index=False)      removes indexing columns
