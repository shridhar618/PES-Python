from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# ----------------------------
# FIX SSL ERROR
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
print("RESPONSE:", type(response))

# ----------------------------
# PARSE HTML
# ----------------------------
soup = bs(response, "html.parser")
print("SOUP:", type(soup))

# ----------------------------
# TITLE
# ----------------------------
print("TITLE:", soup.title)

# ----------------------------
# EXTRACT TABLE ROWS
# ----------------------------
rows = soup.find_all("tr")
print("\nROWS FOUND:", len(rows))

# ----------------------------
# REGEX METHOD – CLEAN DATA
# ----------------------------
regex_rows = []

for row in rows:
    cells = row.find_all("td")
    clean_cells = []

    for c in cells:
        # remove html tags
        text = re.sub("<.*?>", "", str(c))
        # clean remaining html safely
        text = bs(text, "html.parser").get_text(strip=True)
        clean_cells.append(text)

    if clean_cells:
        regex_rows.append(clean_cells)

print("\nREGEX CLEANED ROWS:")
for r in regex_rows:
    print(r)

# ----------------------------
# EXTRACT HEADERS
# ----------------------------
headers = [th.get_text(strip=True) for th in soup.find_all("th")]
print("\nHEADERS:", headers)

# ----------------------------
# CREATE DATAFRAME FROM REGEX DATA
# ----------------------------
if regex_rows:
    df = pd.DataFrame(regex_rows)

    # assign headers only if length matches
    if headers and len(headers) == len(df.columns):
        df.columns = headers
else:
    print("\n⚠️ No data found (site loads data with JavaScript).")
    df = pd.DataFrame()

print("\nDATAFRAME:")
print(df.head())

# ----------------------------
# DROP EMPTY ROWS
# ----------------------------
if not df.empty:
    df = df.dropna(how="all")

# ----------------------------
# CONVERT FINISH TIME TO TOTAL MINUTES
# ----------------------------
def time_to_minutes(t):
    if not isinstance(t, str):
        return None

    parts = t.split(":")

    try:
        if len(parts) == 3:          # HH:MM:SS
            h, m, s = map(int, parts)
            return int(h * 60 + m + s / 60)

        elif len(parts) == 2:        # MM:SS
            m, s = map(int, parts)
            return int(m + s / 60)

        else:
            return int(float(t))
    except:
        return None

# clean column names
if not df.empty:
    df.columns = df.columns.str.strip()

# apply conversion
if not df.empty and "FINISH TIME" in df.columns:
    df["FINISH TIME (MINUTES)"] = df["FINISH TIME"].apply(time_to_minutes)

print("\nFINAL DATAFRAME:")
print(df.head())


#get the mean time taken by each nationality
df5 = df.groupby('NATIONALITY')['FINISH TIME (MINUTES)'].mean().reset_index()