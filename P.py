import gspread
import pywhatkit as kit
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("Copy of CSEA 2020-21").sheet1

col = sheet.col_values(7)
print(col)

message = "This is an automated message sent from the CSEA Whatsapp Bot"

hour=13
minute=11
for x in col:
    if x!="Phone":
        # if minute==60:
            # hour=hour+1
            # minute=1
        kit.sendwhatmsg("+91" + x,message,hour,minute)
        minute=minute+1
        # minute=minute+1