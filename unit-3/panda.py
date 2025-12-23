import pandas as pd

sd=pd.read_csv('sales_demo.csv')
pr=pd.read_csv('products_demo.csv')

print(type(sd), type(pr))

print(sd.shape)

print(pr.shape)

print(sd.columns)

print(pr.columns)

print(pr['ProductID'].nunique())
print(len(pr))

#merge using inner join
df=pd.merge(sd,pr, on='ProductID', how='inner')
print(df.shape)

