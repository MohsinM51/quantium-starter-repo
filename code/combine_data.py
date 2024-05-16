import pandas as pd

data0 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_0.csv')
data1 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_1.csv')
data2 = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/data/daily_sales_data_2.csv')
merged_data = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/code/merged_data.csv')
product_pink_morsels = pd.read_csv('/Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/code/product_pink_morsels.csv')

# product_pink_morsels["price"] = product_pink_morsels["price"].str[1:]
# print(product_pink_morsels.head())
# product_pink_morsels["price"] = product_pink_morsels["price"].astype(float)
# product_pink_morsels['sales'] = product_pink_morsels['price'] * product_pink_morsels['quantity']
# print(product_pink_morsels.head())
#
# product_pink_morsels=product_pink_morsels.to_csv("product_pink_morsels.csv")

# del product_pink_morsels["Unnamed: 0.1"]
# del product_pink_morsels["Unnamed: 0"]
# print(product_pink_morsels)
# product_pink_morsels= product_pink_morsels[['sales','date','region']]
# product_pink_morsels.to_csv('product_pink_morsels.csv')
#
# print(product_pink_morsels.head())