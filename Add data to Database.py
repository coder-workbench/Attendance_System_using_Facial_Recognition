import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-5ec7c-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")
data = {
    "12345":
        {
            "Name": "Anushka Pansare",
            "Major": "AIDS",
            "Starting_year": 2021,
            "Total_attendance": 54,
            "Current_year": 2,
            "Roll_no": "A-09",
            "Last_attendance_time": "2023-05-15 00:20:34"
        },
    "23456":
        {
            "Name": "Ayushi Lanjewar",
            "Major": "AIDS",
            "Starting_year": 2021,
            "Total_attendance": 68,
            "Current_year": 2,
            "Roll_no": "A-14",
            "Last_attendance_time": "2023-05-15 00:25:24"
        },
    "34567":
        {
            "Name": "Gururaj Khule",
            "Major": "AIDS",
            "Starting_year": 2021,
            "Total_attendance": 59,
            "Current_year": 2,
            "Roll_no": "A-74",
            "Last_attendance_time": "2023-05-15 00:30:34"
        },
    "45678":
        {
            "Name": "Akshay Thombare",
            "Major": "AIDS",
            "Starting_year": 2021,
            "Total_attendance": 52,
            "Current_year": 2,
            "Roll_no": "A-03",
            "Last_attendance_time": "2023-05-15 00:34:34"
        },
    "56789":
        {
            "Name": "Ashwini Lanjewar",
            "Major": "MBA",
            "Starting_year": 2021,
            "Total_attendance": 68,
            "Current_year": 2,
            "Roll_no": "A-28",
            "Last_attendance_time": "2023-05-15 00:29:24"
        },
    "67890":
        {
            "Name": "Krishna Karkhanis",
            "Major": "AIDS",
            "Starting_year": 2021,
            "Total_attendance": 38,
            "Current_year": 2,
            "Roll_no": "A-65",
            "Last_attendance_time": "2023-05-15 00:58:24"
        }
}

for key,value in data.items():
    ref.child(key).set(value)