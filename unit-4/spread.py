import gspread as gs

from google.oauth2.service_account import Credentials

from collections import Counter

SERVICE_ACCOUNT='service_account.json'
#Access the downloaded api
SHEET_URL='https://docs.google.com/spreadsheets/d/1yfDX4DxydpN9Rn4_SIGXubPlZxpA7eU6Pf25fmkWt6A/edit?gid=0#gid=0'
#access the google sheet
WORKSHEET_NAME='Sheet1'
#identify the sheet tag to be used
SCOPES=[
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]

def get_preferences():
    creds=Credentials.from_service_account_file(SERVICE_ACCOUNT,scopes=SCOPES)
    client=gs.authorize(creds)
    sheet=client.open_by_url(SHEET_URL)
    worksheet=sheet.worksheet(WORKSHEET_NAME)
    data=worksheet.get_all_records()
    if not data:
        print("No data found in the sheet.")

    header=data[0]
    data_rows=data[1:]
    preferences=[]
    
    if 'ChannelPreference' not in header:
        print("ChannelPreference column not found in the sheet.")
        
        
    idx=header.index('ChannelPreference')
    preferences=[]
    for row in data_rows:
        if len(row)>idx:
            val=row[idx].strip()
            preferences.append(row[idx])
            
            if val!="":
                preferences.append(val)
                
    counts=Counter(preferences)
    for p in preferences:
        print(preferences)
    print('Preference count:')
    for k,v in counts.most_common():
        print(f"Preferences:{k}:{v}")
        
        

            
            
    