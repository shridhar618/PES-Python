#CSV file operation
import csv
#writing to a csv file
with open('students.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 14, 'Grade': '9'})
    writer.writerow({'Name': 'Bob', 'Age': 15, 'Grade': '10'})
    writer.writerow({'Name': 'Charlie', 'Age': 13, 'Grade': '8'})
    
#reading from a csv file
with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        
#appending to a csv file
with open('students.csv', 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writerow({'Name': 'David', 'Age': 16, 'Grade': '11'})
    writer.writerow({'Name': 'Eva', 'Age': 14, 'Grade': '9'})
    
#reading the updated csv file
with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        