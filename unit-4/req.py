import requests as r
import json
import csv

# -------------------------------
# 1. Get single post
# -------------------------------
response = r.get('https://dummyjson.com/posts/120')

print(type(response))
print(response)

# Check if the request was successful
if response.status_code == 200:
    print('Request Successful')
else:
    print(f"Request failed: {response.status_code}")

print(type(response.text), response.text)

data = response.json()
print(f"Post Title: {data['title']}")
print(f"Post User: {data['userId']}")

print("\n\n")

# -------------------------------
# 2. Write single API data into JSON file
# -------------------------------
response = r.get("https://dummyjson.com/posts/121")
data = response.json()

print(data)
print(type(data))

# Save the data to JSON file
with open('api_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print('Data saved to file.')
print("\n\n")

# -------------------------------
# 3. Write multiple API data into JSON file
# -------------------------------
response = r.get('https://dummyjson.com/posts')
data = response.json()

print(data)

posts_list = []
for post in data['posts']:
    posts_list.append({
        'id': post['id'],
        'title': post['title'],     # fixed typo
        'body': post['body'],
        'userId': post['userId'],
        'reactions': post['reactions']
    })

print(posts_list)

# Store in JSON file
with open('api_data_1.json', 'w') as f:
    json.dump(posts_list, f, indent=4)

print('Multiple records saved successfully.')

# -------------------------------
# 4. Save one post into CSV file
# -------------------------------
# Take first post from the list
first_post = data['posts'][0]

with open('api_data.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'Title', 'Body', 'UserId'])
    writer.writerow([
        first_post['id'],
        first_post['title'],
        first_post['body'],
        first_post['userId']
    ])

print('Data stored in CSV file successfully.')