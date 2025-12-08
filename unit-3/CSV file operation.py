#CSV file operation
import csv
#writing to a csv file
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 14, 'Grade': '9'})
    writer.writerow({'Name': 'Bob', 'Age': 15, 'Grade': '10'})
    writer.writerow({'Name': 'Charlie', 'Age': 13, 'Grade': '8'})
    
#reading from a csv file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        print(row)
        
#appending to a csv file
with open('data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writerow({'Name': 'David', 'Age': 16, 'Grade': '11'})
    writer.writerow({'Name': 'Eva', 'Age': 14, 'Grade': '9'})
    
#reading the updated csv file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        
        
#reading from a csv file with different delimiter and skipinitialspace
with open('data1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', skipinitialspace=True)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        print(row)
        
        
#reading from a csv file with different delimiter, skipinitialspace and custom fieldnames
with open('data2.csv', 'r') as csvfile:
    fnames=['Name', 'Age', 'Grade']
    reader = csv.DictReader(csvfile, fieldnames=fnames, delimiter=';', skipinitialspace=True)
    for row in reader:
        print(row)
        
        
data=[
    ['name','age','city'],
    ['Abbot',11,'New York'],
    ['Ben',12,'Los Angeles'],
    ['Charlie',13,'Chicago']
]
#writing to a csv file using writer
with open('data3.csv', 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(data)
    writer.writerow(['David',14,'Houston'])
    writer.writerow(['Eva',15,'Phoenix'])
    
    
#assuming that u have a csv file as employee details that consist of name, emp id, dept, salary. read the file and compute the following values DA which is 18% of salary, HRA which is 2% of salary create an output file emp sal.csv where emp_id,HRA,DA, gross salary return back
import csv

# Open the input CSV file
with open('employee_details.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    
    # Define the fieldnames for the output file
    fieldnames = ['emp_id', 'HRA', 'DA', 'Gross_Salary']
    
    # Open the output CSV file
    with open('emp_sal.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process each row
        for row in reader:
            salary = float(row['salary'])
            da = 0.18 * salary  # 18% of salary
            hra = 0.02 * salary  # 2% of salary
            gross = salary + da + hra
            
            writer.writerow({
                'emp_id': row['emp_id'],
                'HRA': round(hra, 2),
                'DA': round(da, 2),
                'Gross_Salary': round(gross, 2)
            })

print("✅ emp_sal.csv file created successfully!")


        

        