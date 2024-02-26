from pprint import pprint

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1IEFWe6d1A54NT6dSCJqYukgPAaKHdDQygHQ_T9peIqY'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)


# Функция записи значенийв в таблицу Дохода
def add_incase(date, category, price, comment):
    range = 'Доход!A:Z'

    rows = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range).execute().get('values', [])
    last_row_id = len(rows) + 1

    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"Доход!A{last_row_id}:D{last_row_id}",
                 "majorDimension": "ROWS",
                 "values": [[date, category, price, comment]]}
            ]
        }
    ).execute()

    pprint(values)


# Функция записи значенийв в таблицы расходов
def add_expenses(podcategory, date, category, price, comment):
    range = f'{podcategory}!A:Z'

    rows = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range).execute().get('values', [])
    last_row_id = len(rows) + 1

    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"{podcategory}!A{last_row_id}:D{last_row_id}",
                 "majorDimension": "ROWS",
                 "values": [[date, category, price, comment]]}
            ]
        }
    ).execute()

    pprint(values)
