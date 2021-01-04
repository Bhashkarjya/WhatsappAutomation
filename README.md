# WhatsappAutomation
A python script to send automated messages via Whatsapp at specific instance of time by extracting phone numbers from Google Sheets. 

#API Used
The script is using two APIs, the Google Drive API and the Google Sheets API

# Steps to run the script
1. Go to Google Cloud Console and make a new project https://console.cloud.google.com/
2. Navigate to APIs and Services. First enable Google Drive API.
3. Now you need to add credentials to the Google Drive API. Go to create a Service account and add a service name. Select role as the Editor of the Project. Click on Continue.
4. A JSON file will get downloaded and move that JSON file in under the repository of the project in your local device.
5. Next, enable the Google Sheets API.
6. Open the Google Sheets whose number you want to extract and share it to the email id. The email id is same as the "client-email" in the JSON file.
7. Run the following commands in the terminal.

  pip install pywhatkit
  Read the documentation : https://pypi.org/project/pywhatkit/
  
8. The pywhatkit enables you to send message at the specific phone numbers at some instance in time.
9. Run python P.py to run the code
