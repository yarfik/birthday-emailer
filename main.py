import smtplib
import datetime as dt
import random

my_email = "yarfikardiansyah@gmail.com"
my_password = ""
to_email = "yarfik97@yahoo.com"
quotes = []

with open("quotes.txt", "r") as f_quotes:
    quotes = f_quotes.readlines()


def send_email(content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Daily Quote\n\n{content}"
        )


current_date = dt.datetime.now()
day_of_week = current_date.weekday()
if day_of_week in range(0, 7):
    random_quote = random.choice(quotes)
    send_email(random_quote)
    print(random_quote)

# print(current_date.weekday())
