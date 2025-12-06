#XML file operations
import xml.etree.ElementTree as ET
#writing to an XML file
root=ET.Element("students")
student1=ET.SubElement(root, "student")
name1=ET.SubElement(student1, "name")
name1.text="Alice"
age1=ET.SubElement(student1, "age")
age1.text="14"
grade1=ET.SubElement(student1, "grade")
grade1.text="9"
student2=ET.SubElement(root, "student")
name2=ET.SubElement(student2, "name")
name2.text="Bob"
age2=ET.SubElement(student2, "age")
age2.text="15"
grade2=ET.SubElement(student2, "grade")
grade2.text="10"    
tree=ET.ElementTree(root)
tree.write("students.xml")


#reading from an XML file
tree=ET.parse("students.xml")
root=tree.getroot()
for student in root.findall("student"):
    name=student.find("name").text
    age=student.find("age").text
    grade=student.find("grade").text
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
    
#updating an XML file
tree=ET.parse("students.xml")
root=tree.getroot()
for student in root.findall("student"):
    name=student.find("name").text
    if name=="Alice":
        student.find("age").text="15"
tree.write("students.xml")


#reading the updated XML file
tree=ET.parse("students.xml")
root=tree.getroot()
for student in root.findall("student"):
    name=student.find("name").text
    age=student.find("age").text
    grade=student.find("grade").text
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
    
#appending to an XML file
tree=ET.parse("students.xml")
root=tree.getroot()
student3=ET.SubElement(root, "student")
name3=ET.SubElement(student3, "name")
name3.text="Charlie"
age3=ET.SubElement(student3, "age")
age3.text="13"
grade3=ET.SubElement(student3, "grade")
grade3.text="8"    
tree.write("students.xml")


#reading the appended XML file
tree=ET.parse("students.xml")
root=tree.getroot()
for student in root.findall("student"):
    name=student.find("name").text
    age=student.find("age").text
    grade=student.find("grade").text
    print(f"Name: {name}, Age: {age}, Grade: {grade}")  
    
    
    