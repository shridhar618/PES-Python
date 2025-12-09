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
