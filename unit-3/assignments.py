import csv

with open('students.csv', 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    with open('student_summary.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['RollNo', 'Name', 'AverageMarks', 'Result'])

        for row in reader:
            rollno = row[0]
            name = row[1]
            marks = list(map(int, row[2:]))

            avg = sum(marks) / len(marks)
            result = 'Pass' if avg >= 40 else 'Fail'

            writer.writerow([rollno, name, round(avg, 2), result])
            
            
            
            
            
            
import csv

region_sales = {}

with open('daily_sales.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        region = row['Region']
        amount = float(row['Amount'])

        region_sales[region] = region_sales.get(region, 0) + amount

with open('region_sales.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Region', 'TotalSales'])

    for region, total in region_sales.items():
        if total >= 50000:
            writer.writerow([region, total])





import pandas as pd

df = pd.read_excel('attendance.xlsx')

df['AttendancePercentage'] = (df['DaysPresent'] / df['TotalDays']) * 100
df['AttendanceStatus'] = df['AttendancePercentage'].apply(
    lambda x: 'Shortage' if x < 75 else 'OK'
)

df.to_excel('attendance_report.xlsx', index=False)





import pandas as pd

df = pd.read_excel('emp_data.xlsx')

df['HRA'] = df['BasicSalary'] * 0.10
df['DA'] = df['BasicSalary'] * 0.18
df['GrossSalary'] = df['BasicSalary'] + df['HRA'] + df['DA']

result = df[['EmpID', 'Name', 'GrossSalary']]
result.to_excel('emp_salary.xlsx', index=False)




import csv

with open('inventory.csv', 'r') as infile:
    reader = csv.DictReader(infile)

    with open('reorder_list.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['ProductID', 'ProductName', 'Stock'])

        for row in reader:
            if int(row['Stock']) < int(row['ReorderLevel']):
                writer.writerow([
                    row['ProductID'],
                    row['ProductName'],
                    row['Stock']
                ])






import csv

marks = {}

with open('marks1.csv', 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        marks[row['RollNo']] = {
            'Name': row['Name'],
            'Marks1': int(row['Marks1'])
        }

with open('marks2.csv', 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        marks[row['RollNo']]['Marks2'] = int(row['Marks2'])

with open('final_result.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['RollNo', 'Name', 'TotalMarks'])

    for rollno, data in marks.items():
        total = data['Marks1'] + data['Marks2']
        writer.writerow([rollno, data['Name'], total])
        
        
        
import pandas as pd

# Read Excel file
df = pd.read_excel('expenses.xlsx')

# Calculate total per category
summary = df.groupby('Category')['Amount'].sum().reset_index()

# Write to new Excel file
summary.to_excel('monthly_summary.xlsx', index=False)





import csv
import pandas as pd

data = []
fare_list = []

with open('bus_pass_requests.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dist = float(row['Distancekm'])

        if dist <= 5:
            fare = 400
        elif dist <= 10:
            fare = 650
        else:
            fare = 900

        row['Fare'] = fare
        row['Status'] = 'Pending'
        data.append(row)

        fare_list.append([row['ReqID'], row['StudentID'], fare])

pd.DataFrame(data).to_excel('bus_pass_status.xlsx', index=False)

with open('bus_pass_fare_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ReqID', 'StudentID', 'Fare'])
    writer.writerows(fare_list)




import pandas as pd

df = pd.read_excel('returns.xlsx')

valid_modes = ['UPI', 'CARD', 'WALLET']
valid_rows = []
error_rows = []

for _, row in df.iterrows():
    if row['RefundMode'] not in valid_modes:
        row['ErrorReason'] = 'Invalid RefundMode'
        error_rows.append(row)
    elif row['Amount'] <= 0:
        row['ErrorReason'] = 'Invalid Amount'
        error_rows.append(row)
    else:
        valid_rows.append(row)

pd.DataFrame(valid_rows).to_csv('returns_clean.csv', index=False)
pd.DataFrame(error_rows).to_excel('returns_error_log.xlsx', index=False)






import pandas as pd

df = pd.read_excel('returns.xlsx')

valid_modes = ['UPI', 'CARD', 'WALLET']
valid_rows = []
error_rows = []

for _, row in df.iterrows():
    if row['RefundMode'] not in valid_modes:
        row['ErrorReason'] = 'Invalid RefundMode'
        error_rows.append(row)
    elif row['Amount'] <= 0:
        row['ErrorReason'] = 'Invalid Amount'
        error_rows.append(row)
    else:
        valid_rows.append(row)

pd.DataFrame(valid_rows).to_csv('returns_clean.csv', index=False)
pd.DataFrame(error_rows).to_excel('returns_error_log.xlsx', index=False)
