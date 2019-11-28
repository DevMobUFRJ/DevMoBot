import pickle
import os.path
from googleapiclient.discovery import build

class MembersRegister:
    MEMBERS_SPREADSHEET = '1uaHbW_n8U5W_2kHvUTdz9utDZ0hq0fYmtodBPwal7ZA'
    TELEGRAM_USERNAMES = 'Membros Ativos!I2:I'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    def __init__(self):
        if os.path.exists('token.pickle'):
            creds = pickle.load(open('token.pickle', 'rb'))
            service = build('sheets', 'v4', credentials=creds)
            self.sheet = service.spreadsheets()
            return
        raise Exception("Rode o step 3 https://developers.google.com/sheets/api/quickstart/python?authuser=1 e copie o token.pickle para essa pasta")
    
    def getTelegramUsernames(self):
        result = self.sheet.values().get(spreadsheetId=self.MEMBERS_SPREADSHEET, range=self.TELEGRAM_USERNAMES).execute()
        values = result.get('values', [])
        return [row[0] for row in values]
