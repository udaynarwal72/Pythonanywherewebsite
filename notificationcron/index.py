import firebase_admin
from firebase_admin import credentials
from firebase import firebase
from firebase_admin import messaging
# from studease.models import RollNumber
# from django.contrib.auth.models import User
import requests
cred = credentials.Certificate("/Users/udaynarwal/Desktop/studease_main/notificationcron/studease-8b02a-firebase-adminsdk-8ittj-50a56775a2.json")
firebase_admin.initialize_app(cred)
my_token = "dzOo2EcVKB5OTuPxtULPEa:APA91bE-UCiYd9zsTIUUwaHSUcaFU7ijtGedXtESAbX13Uxd2-dsxia6MBf7vbPBq1_WVtyZ2Zi-eTle4_OaP_dDjKHrmL8B7Wfv29UYCvhKXZFfDvaE4MTxld70PgC5MK353yYMI_PY"

def sendNotification(token=my_token, details="E101 INTEGRAL CALUCUS AND DIFFERENCE EQUATIONS-L MAIC 102"): 
    message = messaging.Message(
        token = token,
        data = {
            "title": "Class Notifcation",
            'body': details,
            "icon": "/img/icon.png",
            "link_url": "http://localhost:5001" 
        }
    )
    try: 
        print("Job Executed")
        response = messaging.send(message)
    except:
        pass

def sendNoti():
    api_url = "http://127.0.0.1:8000/getclassdetailbysectioname"
    # current_user= User
    # print(User.username)
    # dummy_sub_section_rollnumber = RollNumber.objects.filter(roll_number=User.username)
    # rollnumber_sub_section = dummy_sub_section_rollnumber.values('sub_section_id')
    # print(rollnumber_sub_section)
    data = {
        'sub_section_id' : 48
    }
    try:
        # Make the POST request
        response = requests.post(api_url, json=data)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            data = response.json()
            print(data)
            tokens = data["tokens"]
            detail = data["details"]
            for token in tokens:
                if(len(token) > 0): 
                    print(token)
                    sendNotification(token, detail)
        else:
            print(f"Request failed with status code {response.status_code} ")
            print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e} ")

sendNotification()