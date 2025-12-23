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

 
m_inner=pd.merge(pr,sd, on='ProductID', how='inner')

m_left=pd.merge(pr,sd, on='ProductID', how='left')
m_left1=pd.merge(sd,pr, on='ProductID', how='left')
print(m_left.shape, m_left1.shape)
print(m_left)

m_right=pd.merge(pr,sd, on='ProductID', how='right')
m_right1=pd.merge(sd,pr, on='ProductID', how='right')
print(m_right.shape, m_right1.shape)
print(m_right)

m_outer=pd.merge(pr,sd, on='ProductID', how='outer')
m_outer1=pd.merge(sd,pr, on='ProductID', how='outer')
print(m_outer.shape, m_outer1.shape)
print(m_outer)


