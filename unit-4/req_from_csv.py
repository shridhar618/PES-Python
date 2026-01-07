import requests as req
import csv

response=req.get("https://dummyjson.com/posts")
data=response.json()
print(data)

posts=data['posts']
print(type(posts), posts)



with open('api_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Id', 'Title', 'UserId', 'Views'])  # Write header row
    for p in posts:
        writer.writerow([p['id'], p['title'], p['userId'], p['views']])  # Write data rows
        
print("Data written to api_data.csv successfully.")