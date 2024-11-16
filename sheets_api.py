from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

from dotenv import load_dotenv
load_dotenv()

# Define the scope and spreadsheet details
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = 'your_spreadsheet_id'
RANGE_NAME = 'Sheet1!A1:E10'

# Load credentials and create the service
creds = Credentials.from_service_account_file('GOOGLE_APPLICATION_CREDENTIALS', scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Fetch the data from the spreadsheet
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
rows = result.get('values', [])
print(rows)