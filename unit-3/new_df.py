import pandas as pd

df=pd.read_csv('sales_r.csv')

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head(2))
print(df.tail(3))

#CHeck for NAN values
print(df.isna())
print(df.isna().sum())

#Check NAN in rows
print(df.isna().any(axis=1))
print(df.isna().any(axis=1).sum())

#Check for not NAN values in columns
print(df.notna())
print(df.notna().sum())

#Check for not NAN values in ROws

print(df.notna().any(axis=1))
print(df.notna().any(axis=1).sum())

print(df.columns)

#Clean the column names.
df.columns=df.columns.str.strip()
print(df.columns)

print(df.head)
print(df.tail)

#Remove a quotes, commas from a particular column.


#Convert column amount to str
#Replace quotes
#Replace comma
#Extract the numeric digits.

df['Amount']=(
    df['Amount'].astype(str)
    .str.replace('"','',regex=False)
    .str.replace(',','',regex=False)
    .str.extract(r'(\d+)',expand=False)
)

print(df.dtypes)

#NAN values can be replaced with
# 1. mean-mid value
# 2. median- avg value
# 3. mode- value with hightest freq

#Convert column to Numeric

df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
    #first parameter - column that has to be converted
    #errors = coerce -all non numeric chars will be converted as NAN
print(df.dtypes)

#Fill NaN Values with median

df['Amount']=df['Amount'].fillna(df["Amount"].median())
print(df['Amount'])

print(df['Qty'])

#Replace in Qty with mean
df['Qty']=pd.to_numeric(df['Qty'],errors='coerce')

print(df.dtypes)
print(df['Qty'])

#Fill Qty's NaN valuess with mean
df['Qty']=df['Qty'].fillna(df['Qty'].mean())
print(df['Qty'])

print(df.head)

#Drop Columns
# 1. If the column contains too many NAN
# 2. it is unwanted column


df=df.dropna(axis=1, how='all')
print(df.columns)

df=df.dropna(axis=1, how='any')
print(df.columns)

# df=df.drop(columns=['Unnamed: 6'])

df=df.iloc[:,:-1] #This works only for last columns.
df=df.loc[:,~df.columns.str.contains('^Unnamed')] #works when the exact column name is not known
print(df)



print(df['Region'])


#standardize text columns
df['Region']=df['Region'].str.strip().str.lower()

print(df['Region'])

#Remove quotes in all cols
df=df.apply(lambda c: c.astype(str).str.replace('"','',regex=False))
print(df)


df.loc[pd.to_numeric(df['Region'],errors='coerce').isin([500,800]),'Region']='north'
print(df['Region'])
print(df)


# #convert the region to numeric. all non numeric values will be converted to NAN
# df['Region']=pd.to_numeric(df['Region'],errors='coerce')
# print(df['Region'])
# print(df.dtypes)
# #create a bulean mask. it is true when region is 500 or 800
# mask=pd.to_numeric(df['Region'],errors='coerce').isin([500,800])
# print(mask)
# #replace all such rows with region as north
# df.loc[mask,'Region']='north'
# print(df['Region'])
# print(df)


#filter data based opn conditions
df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
hsales=df['Amount']>2000

print(type(hsales))
print(hsales)

#cxreate a new dataframe based on the filter
df_high=df[hsales]
print(type(df_high))
print(df_high)


#to count the number of records in a df
print(len(df))
print(len(df_high))


#filktereing based on multiple conditions
c_amt=df['Amount']>2000
c_reg=df['Region']=='south'
print(type(c_amt), type(c_reg))

#condions can be combined using & (and), | (or) operators
df_t1=df[c_amt & c_reg]
print(df_t1)
print(len(df_t1))  
 
df_t2=df[c_amt | c_reg]
print(df_t2)
print(len(df_t2))

df_t3=df[~c_reg]
print(df_t3)



#sort the values in columns
df_sorted=df.sort_values(by='Amount')
print(df_sorted)
#default order is ascending

df_sorted_desc=df.sort_values(by='Amount', ascending=False)
print(df_sorted_desc)


df_sorted1=df.sort_values(['Region','Amount'])
print(df_sorted1)

df_sorted2=df.sort_values(['Region','Amount'], ascending=[True,False])
print(df_sorted2)

#create new column based on exsting columns
df['Tax']=df['Amount']*0.18
print(df.columns)


df['Total_Amount']=df['Amount']+df['Tax']
print(df.columns, df.dtypes)
print(df)

#count the values
print(df['Region'].value_counts())
print(df['Amount'].value_counts())

#summerize the dataframe
print(df['Amount'].describe())

print(df['Region'].describe())

print(df['Qty'].describe())

print(df['Tax'].describe())

print(df['Total_Amount'].describe())


#grouing the data
grp_reg=df.groupby('Region')
print(type(grp_reg))
print(grp_reg)


#view the group data
#1.view the group names
print(grp_reg.groups.keys())
#2.view the row index that belong to each group
print(grp_reg.groups)
#3.get a specific group
print(grp_reg.get_group('north'))
print(grp_reg.get_group('south'))
#4.loop tghrough each group
for name, group in grp_reg:
    print(f"Group Name: {name}")
    print(group)
#5.grouping based on multiple columns
grp_multi=df.groupby(['Region','Product'])
print(type(grp_multi))
print(grp_multi.groups.keys())

#6.sum of the amount of each region
#aggregation
sales_reg=grp_reg['Amount'].sum()
print(sales_reg)

#7.multiple aggregation
region_summary=grp_reg['Amount'].agg(['sum','mean','count'])
print(region_summary)

#8.custom aggregation
summary=df.groupby('Region').agg(
    Total_Amt=('Amount','sum'),
    Avg_Amt=('Amount','mean'),
    Avg_tax=('Tax','mean'),
    Count_Records=('Amount','count'),
    Unique_Products=('Product','nunique')
)
print(type(summary))
print(summary)