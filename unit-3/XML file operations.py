#XML file operations
import xml.etree.ElementTree as xml

# #writing to an XML file
# root=xml.Element("students")
# student1=xml.SubElement(root, "student")
# name1=xml.SubElement(student1, "name")
# name1.text="Alice"
# age1=xml.SubElement(student1, "age")
# age1.text="14"
# grade1=xml.SubElement(student1, "grade")
# grade1.text="9"
# student2=xml.SubElement(root, "student")
# name2=xml.SubElement(student2, "name")
# name2.text="Bob"
# age2=xml.SubElement(student2, "age")
# age2.text="15"
# grade2=xml.SubElement(student2, "grade")
# grade2.text="10"    
# tree=xml.ElementTree(root)
# tree.write("students.xml")


# #reading from an XML file
# tree=xml.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     age=student.find("age").text
#     grade=student.find("grade").text
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
    
# #updating an XML file
# tree=xml.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     if name=="Alice":
#         student.find("age").text="15"
# tree.write("students.xml")


# #reading the updated XML file
# tree=xml.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     age=student.find("age").text
#     grade=student.find("grade").text
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
    
# #appending to an XML file
# tree=xml.parse("students.xml")
# root=tree.getroot()
# student3=xml.SubElement(root, "student")
# name3=xml.SubElement(student3, "name")
# name3.text="Charlie"
# age3=xml.SubElement(student3, "age")
# age3.text="13"
# grade3=xml.SubElement(student3, "grade")
# grade3.text="8"    
# tree.write("students.xml")


# #reading the appended XML file
# tree=xml.parse("students.xml")
# root=tree.getroot()
# for student in root.findall("student"):
#     name=student.find("name").text
#     age=student.find("age").text
#     grade=student.find("grade").text
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")  
    
    
    
    
books=[
    {'Title':'Pride and Prejudice', 'Author':'Jane Austen', 'Price':240, 'Category':'Fiction'},
    {'Title':'The Diary of a Young Girl', 'Author':'Anne Frank', 'Price':500, 'Category':'Non-Fiction'}
]

#create the root element
root=xml.Element("books")
print(type(root))
for book in books:
    book_elem=xml.Element("book")
    for key, val in book.items():
        child=xml.SubElement(book_elem, key)
        child.text=str(val)
    root.append(book_elem)
    
    
for book in books:
    book_elem=xml.Element("book")
    for key, val in book.items():
        child=xml.SubElement(book_elem, key)
        child.text=str(val)
    root.append(book_elem)
    title=book_elem.find("Title").text
    author=xml.SubElement(book_elem, "Author")
    
tree=xml.ElementTree(root)
    
    
with open('books.xml',"wb") as fh:
    tree.write(fh)
    
print("Books.xml file has been created")


print(type(book_elem),type(title),type(author))


tree=xml.ElementTree(file='books.xml')
root=tree.getroot()
books=[]
print(type(tree), type(root), type(books))

for book in root.findall("book"):
    b_data={}
    b_data['Category']=book.get('Category')#get the attributes and its values
    for d in book:#get each child element for every parent
        b_data[d.tag]=d.text
    books.append(b_data)
print(type(book), type(b_data), type(d))
print(books)


#modification of a xml file
tree=xml.ElementTree(file='books.xml')
root=tree.getroot()
#iterate over price
for p_ele in root.iter('Price'):
    p=int(p_ele.text)
    p+=20
    p_ele.text=str(p)
#write the new data back into xml file
with open('books.xml',"wb") as f:
    tree.write(f)
print("Price updated")
    
    
#wite an xml file called as emp.xml it contains name, age and salary of every employee. once the xml file is created, modify the existing sal by increasing it by 5%. update the file and show the changed salary.
employees=[
    {'Name':'John Doe', 'Age':'30', 'Salary':'50000'},
    {'Name':'Jane Smith', 'Age':'25', 'Salary':'60000'}
]

#creating emp.xml
root=xml.Element("employees")
for emp in employees:
    emp_elem=xml.Element("employee")
    for key, val in emp.items():
        child=xml.SubElement(emp_elem, key)
        child.text=str(val)
    root.append(emp_elem)
tree=xml.ElementTree(root)
with open('emp.xml',"wb") as fh:
    tree.write(fh)
print("emp.xml file has been created")
#modifying salary by increasing 5%
tree=xml.ElementTree(file='emp.xml')
root=tree.getroot()
for sal_ele in root.iter('Salary'):
    sal=int(sal_ele.text)
    sal+=sal*0.05
    sal_ele.text=str(int(sal))
with open('emp.xml',"wb") as f:
    tree.write(f)
print("Salary updated in emp.xml")

    

    
    