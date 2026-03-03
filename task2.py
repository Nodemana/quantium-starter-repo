import pandas as pd

df = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

df = pd.concat([df, df2, df3])

# filter the dataframe to only include rows where the product is 'pink morsel'
df = df[df['product'] == 'pink morsel']
df['sales'] = df['price'].str.strip('$').astype(float) * df['quantity'].astype(int)
df.drop(columns=['price', 'quantity'], inplace=True)

print(df.head())

print(df.tail())