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

#combine two dataframes vertically
s1=pd.read_csv('sales.csv')
s2=pd.read_csv('sales_q2.csv')

#check whether two dataframes have same structure
print(s1.shape, s2.shape)
print(s1.columns)
print(s2.columns)

s_all=pd.concat([s1,s2], ignore_index=True)
s_all1=pd.concat([s1,s2])
print(s_all.shape)
print(s_all1.shape)

print(s_all.head())
print(s_all)
print(s_all1)


#export the dataframe 
s_all.to_csv('sales_all.csv', index=False)
s_all.to_csv('sales_all_1.csv')

s_all1.to_excel('sales_all.xlsx', index=False)
# s_all1.to_json('sales_all.json')
# s_all.to_xml('sales_all.xml', index=False)
s_all.to_html('sales_all.html')