from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# ----------------------------
# FIX SSL ERROR (important on macOS)
# ----------------------------
context = ssl._create_unverified_context()

# ----------------------------
# URL
# ----------------------------
url = "https://tatamumbaimarathon.procam.in/results/race-results"

# ----------------------------
# OPEN WEBPAGE
# ----------------------------
response = urlopen(url, context=context)
print(type(response))

# ----------------------------
# PARSE HTML
# ----------------------------
soup = bs(response, "lxml")
print(type(soup))

# ----------------------------
# TITLE
# ----------------------------
title = soup.title
print(title)
print(type(title))

# ----------------------------
# PAGE TEXT
# ----------------------------
text = soup.get_text()
print(type(text))
# print(text)   # (optional – very large output)

# ----------------------------
# EXTRACT LINKS
# ----------------------------
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))

# ----------------------------
# EXTRACT TABLE ROWS
# ----------------------------
rows = soup.find_all("tr")
print("\nROWS FOUND:", len(rows))
print(type(rows))

# ----------------------------
# GET ALL TABLE DATA
# ----------------------------
table_data = []

for row in rows:
    cols = row.find_all("td")
    cols = [col.get_text(strip=True) for col in cols]
    if cols:
        table_data.append(cols)

# ----------------------------
# SHOW RAW TABLE DATA
# ----------------------------
print("\nTABLE DATA:")
for row in table_data:
    print(row)

# ----------------------------
# CONVERT TO DATAFRAME (CORRECT WAY)
# ----------------------------
if table_data:
    df = pd.DataFrame(table_data)
    print("\nDATAFRAME:")
    print(df.head())
else:
    print("\nNo table data found (page is JS based).")

# ----------------------------
# CLEAN HTML USING BEAUTIFULSOUP (not regex)
# ----------------------------
if rows:
    str_cells = str(rows)
    cleaned_text = bs(str_cells, "lxml").get_text()
    print("\nCLEANED TEXT:")
    print(cleaned_text[:500])   # show first 500 chars
    print(type(cleaned_text))

# ----------------------------
# REGEX METHOD (your way – fixed)
# ----------------------------
list_rows = []

for row in rows:
    cells = row.find_all("td")
    str_cells = str(cells)
    clean = re.compile("<.*?>")
    clean_text = re.sub(clean, "", str_cells)
    if clean_text.strip():
        list_rows.append(clean_text)

print("\nREGEX CLEANED ROWS:")
print(list_rows)

#remove the opening square bracket
df1 = pd.DataFrame(list_rows)
df1[0] = df1[0].str.lstrip('[')
print("\nDATAFRAME FROM REGEX METHOD:")
print(df1.head())


#remove the closing square bracket
df1[0] = df1[0].str.rstrip(']')
print("\nDATAFRAME AFTER REMOVING CLOSING BRACKET:")
print(df1.head())


#get the headers for the columns
col_labels = soup.find_all("th")
print(col_labels)
print("\n\n")
print(type(col_labels))
all_header = []
col_str=str(col_labels)
clean_text=bs(col_str,"lxml").get_text()
all_header.append(clean_text)
print("\nCLEANED HEADERS:")
print(all_header)


df2 = pd.DataFrame(all_header)
print(df2)

df3=df2[0].str.split(',',expand=True)
print("\nSPLIT HEADERS DATAFRAME:")
print(df3.head())

df3[0]=df3[0].str.strip('[')
df3[4]=df3[4].str.strip(']')
print("\nCLEANED SPLIT HEADERS DATAFRAME:")
print(df3.head())


#merge two dataframes
frames=[df3,df1]
df4=pd.concat(frames,ignore_index=True)
print("\nMERGED DATAFRAME:")
print(df4.head())

#assingn the first row as header
df5=df4.rename(columns=df4.iloc[0]).drop(df4.index[0])
print("\nFINAL DATAFRAME WITH HEADERS:")
print(df5.head())


#drop all rows with missing values
df6=df5.dropna(axis=0, how='any')
print("\nDATAFRAME AFTER DROPPING ROWS WITH MISSING VALUES:")
print(df6.head())


#drop row 1
df5=df5.drop(index=1)
print("\nDATAFRAME AFTER DROPPING ROW 1:")
print(df5.head())

