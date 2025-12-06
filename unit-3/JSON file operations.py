#JSON file operations
import json
#writing to a json file
data={"name":"John", "age":30, "city":"New York"}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    
#reading from a json file
with open('data.json', 'r') as jsonfile:
    data_loaded=json.load(jsonfile)
    print(data_loaded)
    
#updating a json file
with open('data.json', 'r+') as jsonfile:
    data=json.load(jsonfile)
    data['age']=31
    jsonfile.seek(0)
    json.dump(data, jsonfile)
    jsonfile.truncate()
    
#reading the updated json file
with open('data.json', 'r') as jsonfile:
    data_loaded=json.load(jsonfile)
    print(data_loaded)
    
#appending to a json file
with open('data.json', 'r+') as jsonfile:
    data=json.load(jsonfile)
    data['country']='USA'
    jsonfile.seek(0)
    json.dump(data, jsonfile)
    jsonfile.truncate()
    
#reading the appended json file
with open('data.json', 'r') as jsonfile:
    data_loaded=json.load(jsonfile)
    print(data_loaded)
    
    
    