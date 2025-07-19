from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("Your own email id")
MY_PASSWORD = os.getenv("Your password(You don't have to put your email password here. "
               "You have to create a app password on you mail platform in the security tab."
               "It will give you a random password copy that password and place it here.")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthday_dict= {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.itterows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents= contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("Your mail platform SMTP you can. Just google it ") as mail_platform:
        mail_platform.starttls()
        mail_platform.login(MY_EMAIL, MY_PASSWORD)
        mail_platform.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: As per your choice\n\n{contents}"
        )