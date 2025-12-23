#pandas-dataframes
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [14, 15, 13, 16],
    'Grade': [9, 10, 8, 11]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nDataFrame Info:")
df.info()
print("\nDataFrame Description:")
print(df.describe())

# Accessing specific columns
print("\nNames Column:")
print(df['Name'])

# Accessing specific rows
print("\nFirst Two Rows:")
print(df.iloc[0:2])

# Filtering data
print("\nStudents older than 14:")
print(df[df['Age'] > 14])

# Adding a new column
df['Passed'] = [True, True, True, False]
print("\nDataFrame with Passed Column:")
print(df)

# Saving DataFrame to a CSV file
df.to_csv('students.csv', index=False)
 
# Reading DataFrame from a CSV file
df_from_csv = pd.read_csv('students.csv')
print("\nDataFrame read from CSV:")
print(df_from_csv)


#Create another DataFrame
data2={'Name':['Amora','Beast','Captain America','Daredevil'],
      'Age':[25,30,35,40],
      'City':['New York','Los Angeles','Chicago','Houston']
      }

df2=pd.DataFrame(data2)
print(type(data2), type(df2))
print("\nNew DataFrame:")
print(df2)

#create a dataframe from a list
data3=[['Eve',28,'Miami'],['Frank',33,'Seattle'],['Grace',29,'Boston']]
df3=pd.DataFrame(data3)
print("\nDataFrame from List:")
print(df3)





# df5=pd.read_csv('data.csv')
# print(df5)

# df6=pd.read_excel('data.xlsx')
# print(df6)

# df7=pd.read_json('data.json')
# print(df7)

# df8=pd.read_html('data.html')
# print(df8[0])  #printing the first table found in the HTML file

# df8=pd.DataFrame()
# print(df8)  


#inspection methods
# df7.head()
# df7.tail()
# df7.info()
# df7.describe()
# df7.shape()
# df7.columns()

print(df.shape)
print(df.columns)
print(df.isna().any())
print(df.isna().any(axis=1))
print(df.isna().any(axis=1).sum())
print(df.notna().any(axis=1).sum())


#Clean the column names
df.columns=df.columns.str.strip().str.lower().str.replace(' ','_').str.replace('(','').str.replace(')','')
print(df.columns)


print(df.dtypes)


#equivalent commands 
df=df.drop(columns=['passed'])
print(df)



df=df.iloc[:,:-1]
#drop column by column positions 
#drop the last column
print(df)


df=df.loc[:, df.columns!='age']
#drop column by column names
print(df)

#standardize text columns
data4={'Name':['  Alice  ','  Bob','Charlie  ','  David  '],
      'City':[' New York ','Los Angeles ',' Chicago',' Houston ']
      } 
df4=pd.DataFrame(data4)
print("\nDataFrame before standardizing text columns:")
print(df4)  
df4['Name']=df4['Name'].str.strip().str.title()
print("\nDataFrame after standardizing text columns:")
print(df4)


#remove quotes in all columns
df = df4.apply(lambda c: c.str.replace('"', '', regex=False))
print("\nDataFrame after removing quotes:")
print(df)



