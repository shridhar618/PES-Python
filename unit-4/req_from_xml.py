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