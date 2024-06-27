import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "yarfikardiansyah@gmail.com"
my_password = ""


def send_email(destination_name, to_email, content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        msg = f"Subject:Happy Birthday {destination_name}\n\n{content}"
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=msg
        )


def get_letter(person_name):
    file_name = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_name) as letter_file:
        letter_lines = letter_file.readlines()
        letter_lines[0] = letter_lines[0].replace("[NAME]", person_name)
        return "".join(letter_lines)
    return "- Happy Birthday -"


current_date = dt.datetime.now()
day_of_week = current_date.day
month_of_day = current_date.month

df = pd.read_csv("birthdays.csv")
for person_birth in df.itertuples(index=False, name="Person"):
    if day_of_week == person_birth.day and month_of_day == person_birth.month:
        letter = get_letter(person_birth.name)
        send_email(person_birth.name, person_birth.email, letter)
