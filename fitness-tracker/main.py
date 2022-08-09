import requests
from datetime import datetime
import os

NUTRITIONIX_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRI_API_KEY")

TODAY = datetime.now()
AGE = 30
GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 180

exercise_text = input("What exercise did you do? ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
result = response.json()

bearer_header = {
    "Authorization": os.environ.get("BEARER_AUTH")
}

for exercise in result['exercises']:
    exercise_data = {
        "workout": {
            "date": TODAY.strftime("%d/%m/%y"),
            "time": TODAY.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=exercise_data, headers=bearer_header)
    print(sheet_response.text)