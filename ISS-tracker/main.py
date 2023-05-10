# __________________________ISS TRACKER_____________________________ #
# Program tracks the position of the International Space Station (ISS).
# If ISS is above user's location it will send user an email to look up.

import requests
from datetime import datetime
import smtplib
import time

# _____________________ESTABLISH KEY VARIABLES________________#
MY_LAT = "LAT"
MY_LONG = "LONG"
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


# _____________________SEND EMAIL________________#
def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg="Subject:It's Here!\n\n"
                                "Look up! The ISS Station is right above you!")


# _____________________COMPARE TIMES________________#
def compare_times():
    time_now = datetime.now()
    if sunset < time_now.hour < sunrise:
        return True
    else:
        return False


# _____________________COMPARE POSITIONS________________#
def compare_positions():
    if MY_LONG-5 <= iss_long <= MY_LONG+5 and MY_LAT-5 <= iss_lat <= MY_LAT+5:
        return True
    else:
        return False


# _____________________REQUEST AND FORMAT ISS DATA________________#
while True:
    time.sleep(60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    is_above = compare_positions()

    # _____________________REQUEST AND FORMAT SUNRISE AND SUNSET DATA________________#
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4
    is_dark = compare_times()

    if is_dark and is_above:
        send_email()

