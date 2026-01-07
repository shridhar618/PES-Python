import requests as req
import xml.etree.ElementTree as ET

url = "https://dummyjson.com/posts/45"

try:
    response = req.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("API Response:", data)

    root = ET.Element("post")

    # Use .get() to avoid KeyError
    ET.SubElement(root, "id").text = str(data.get("id", "N/A"))
    ET.SubElement(root, "title").text = str(data.get("title", "N/A"))
    ET.SubElement(root, "userId").text = str(data.get("userId", "N/A"))

    tree = ET.ElementTree(root)
    tree.write("api_data.xml", encoding="utf-8", xml_declaration=True)

    print("Data Stored Successfully")

except req.exceptions.ConnectionError:
    print("❌ Internet/DNS problem.")
except req.exceptions.Timeout:
    print("❌ Request timed out.")
except req.exceptions.RequestException as e:
    print("❌ Request failed:", e)
    
    
    
    
import requests as req
import xml.etree.ElementTree as ET

response = req.get("https://dummyjson.com/posts")
data = response.json()

root=ET.Element("posts")

for item in data['posts']:
    post_elem=ET.SubElement(root, "post")
    id_el=ET.SubElement(post_elem, "id")
    id_el.text=str(item['id'])
    
    title_el=ET.SubElement(post_elem, "title")
    title_el.text=str(item['title'])
    
    u_el=ET.SubElement(post_elem, "userId")
    u_el.text=str(item['userId'])
    
    v_el=ET.SubElement(post_elem, "views")
    v_el.text=str(item['views'])
    
    tree=ET.ElementTree(root)
tree.write("api_multiple_data.xml", encoding="utf-8", xml_declaration=True)
print("Multiple Data Stored Successfully")


#Hnadling exceptions during api calls
import requests as req
try:
    response = req.get("https://dummyjson.com/posts/67", timeout=10)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    print("API Response:", data)
    data=response.json()
    print(f"retrieve length of {len(data)} records")

except req.exceptions.HTTPError as e:
    print("HTTP Error occurred.")
    
except req.exceptions.ConnectionError:
    print("Connection Error occurred. Internet/DNS problem.")
    
except req.exceptions.Timeout as e:
    print("The request timed out.")
    
except req.exceptions.RequestException as e:
    print(f"error in meeting the request: {e}")
    
except ValueError:
    print("Error parsing JSON response.")
    
    
print(data)