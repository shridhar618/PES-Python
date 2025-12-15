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


# import xml.etree.ElementTree as ET    
# #creating an XML file
# root=ET.Element("students")
# student1=ET.SubElement(root, "student")
# name1=ET.SubElement(student1, "name")
# name1.text="Alice"
# age1=ET.SubElement(student1, "age")
# age1.text="14"
# grade1=ET.SubElement(student1, "grade")
# grade1.text="9"
# student2=ET.SubElement(root, "student")
# name2=ET.SubElement(student2, "name")
# name2.text="Bob"
# age2=ET.SubElement(student2, "age")
# age2.text="15"
# grade2=ET.SubElement(student2, "grade")
# grade2.text="10"    
# tree=ET.ElementTree(root)
# tree.write("students.xml")

# #reading from an XML file
# tree=ET.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     age=student.find("age").text
#     grade=student.find("grade").text
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
# #updating an XML file
# tree=ET.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     if name=="Alice":
#         student.find("age").text="15"
# tree.write("students.xml")

# #reading the updated XML file
# tree=ET.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     age=student.find("age").text
#     grade=student.find("grade").text
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
# #appending to an XML file
# tree=ET.parse("students.xml")
# root=tree.getroot()
# student3=ET.SubElement(root, "student")
# name3=ET.SubElement(student3, "name")
# name3.text="Charlie"
# age3=ET.SubElement(student3, "age") 
# age3.text="13"
# grade3=ET.SubElement(student3, "grade")
# grade3.text="8"
# tree.write("students.xml")  


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





df5=pd.read_csv('data.csv')
print(df5)

df6=pd.read_excel('data.xlsx')
print(df6)

df7=pd.read_json('data.json')
print(df7)

df8=pd.read_html('data.html')
print(df8[0])  #printing the first table found in the HTML file

df8=pd.DataFrame()
print(df8)  


#inspection methods
df7.head()
df7.tail()
df7.info()
df7.describe()
df7.shape
df7.columns