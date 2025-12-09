# ✅ JSON File Operations
import json

# -------------------------------
# Writing to a JSON file
# -------------------------------
data = {"name": "John", "age": 30, "city": "New York"}

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

print("✅ JSON file 'data.json' created successfully.")

# -------------------------------
# Reading from a JSON file
# -------------------------------
with open('data.json', 'r') as jsonfile:
    data_loaded = json.load(jsonfile)
    print("\n📖 Reading from JSON file:")
    print("Type:", type(data_loaded))
    print("Data:", data_loaded)

# -------------------------------
# Updating a JSON file (modify age)
# -------------------------------
with open('data.json', 'r+') as jsonfile:
    data = json.load(jsonfile)
    data['age'] = 31  # update value
    jsonfile.seek(0)  # move cursor to start
    json.dump(data, jsonfile)
    jsonfile.truncate()  # remove leftover data

print("\n✅ JSON file updated successfully.")

# Verify update
with open('data.json', 'r') as jsonfile:
    data_loaded = json.load(jsonfile)
    print("Updated Data:", data_loaded)

# -------------------------------
# Appending to a JSON file (add country)
# -------------------------------
with open('data.json', 'r+') as jsonfile:
    data = json.load(jsonfile)
    data['country'] = 'USA'  # append new key-value pair
    jsonfile.seek(0)
    json.dump(data, jsonfile)
    jsonfile.truncate()

print("\n✅ JSON file appended successfully.")

# Verify append
with open('data.json', 'r') as jsonfile:
    data_loaded = json.load(jsonfile)
    print("Appended Data:", data_loaded)

# -------------------------------
# Working with Python string and dict
# -------------------------------
p = '{name: "Alice", age: 25, city: "Los Angeles"}'   # ❌ invalid JSON string (single quotes, no quotes on keys)
p1 = {"name": "Alice", "age": 25, "city": "Los Angeles"}  # ✅ correct Python dictionary

print("\n🧩 Data type checks:")
print("Type of p:", type(p))
print("Type of p1:", type(p1))
print("Accessing name:", p1['name'])

# -------------------------------
# Writing and Reading another JSON file
# -------------------------------
with open('data1.json', 'w') as jsonfile:
    json.dump(p1, jsonfile)

print("\n✅ JSON file 'data1.json' written successfully.")

with open('data1.json', 'r') as jsonfile:
    p2_json = json.load(jsonfile)
    print("📖 Reading 'data1.json':")
    print("Type:", type(p2_json))
    print("Data:", p2_json)

print("\n🎯 All JSON operations completed successfully!")

for r in p2_json:
    print("Value:", p2_json[r]) 
    
    
with open('data3.json', 'w') as jsonfile:
    json.dump(p2_json, jsonfile)
    
    
    
#assuming that u have a file called as emp.json that has name, dept, sal.
#display the highest and lowest sal. display the name of the emp who gets highest and lowest sal.
#display the average sal per dept.
import json

# -----------------------------------------
# Step 1: Create sample emp.json (only if not already present)
# -----------------------------------------
sample_data = [
    {"name": "John", "dept": "IT", "sal": 50000},
    {"name": "Maya", "dept": "HR", "sal": 40000},
    {"name": "Arjun", "dept": "Finance", "sal": 45000},
    {"name": "Neha", "dept": "IT", "sal": 55000},
    {"name": "Kiran", "dept": "HR", "sal": 42000}
]

try:
    with open('emp.json', 'x') as f:  # 'x' creates file if not exists
        json.dump(sample_data, f, indent=4)
        print("✅ Created emp.json with sample data.")
except FileExistsError:
    pass  # File already exists — skip creation

# -----------------------------------------
# Step 2: Read data from emp.json
# -----------------------------------------
with open('emp.json', 'r') as f:
    employees = json.load(f)

# -----------------------------------------
# Step 3: Find highest and lowest salary
# -----------------------------------------
highest = max(employees, key=lambda x: x['sal'])
lowest = min(employees, key=lambda x: x['sal'])

print("\n💰 Salary Analysis:")
print(f"Highest Salary: {highest['sal']} (Employee: {highest['name']})")
print(f"Lowest Salary:  {lowest['sal']} (Employee: {lowest['name']})")

# -----------------------------------------
# Step 4: Compute average salary per department
# -----------------------------------------
dept_salaries = {}

for emp in employees:
    dept = emp['dept']
    sal = emp['sal']
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(sal)

print("\n📊 Average Salary per Department:")
for dept, sals in dept_salaries.items():
    avg = sum(sals) / len(sals)
    print(f"{dept:<10} → ₹{avg:.2f}")

# -----------------------------------------
# Step 5: Optional — display nicely as JSON
# -----------------------------------------
summary = {
    "Highest Salary": {"name": highest['name'], "salary": highest['sal']},
    "Lowest Salary": {"name": lowest['name'], "salary": lowest['sal']},
    "Average per Dept": {dept: round(sum(s)/len(s), 2) for dept, s in dept_salaries.items()}
}

with open('emp_summary.json', 'w') as f:
    json.dump(summary, f, indent=4)

print("\n✅ Summary written to emp_summary.json successfully!")

    
    