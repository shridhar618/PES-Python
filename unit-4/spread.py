import gspread as gs
from google.oauth2.service_account import Credentials
from collections import Counter

SERVICE_ACCOUNT = 'service_account.json'

SHEET_URL = 'https://docs.google.com/spreadsheets/d/1yfDX4DxydpN9Rn4_SIGXubPlZxpA7eU6Pf25fmkWt6A/edit?gid=0#gid=0'

WORKSHEET_NAME = 'Sheet1'

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]

def get_preferences():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
    client = gs.authorize(creds)

    sheet = client.open_by_url(SHEET_URL)
    worksheet = sheet.worksheet(WORKSHEET_NAME)

    # This returns a list of dictionaries
    data = worksheet.get_all_records()

    if not data:
        print("No data found in the sheet.")
        return

    preferences = []

    # Check if column exists
    if 'ChannelPreference' not in data[0]:
        print("ChannelPreference column not found in the sheet.")
        return

    # Collect preferences
    for row in data:
        val = row.get('ChannelPreference', '').strip()
        if val:
            preferences.append(val)

    # Count preferences
    counts = Counter(preferences)

    print("Preferences list:")
    print(preferences)

    print("\nPreference count:")
    for k, v in counts.most_common():
        print(f"{k} : {v}")

get_preferences()