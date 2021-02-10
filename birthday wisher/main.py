
from datetime import datetime
import pandas
import smtplib

MY_EMAIL = "webdevbysohag@gmail.com"
MY_PASSWORD = "sohag522000"

today = datetime.now()
today_tuple = (today.month, today.day)
this_year=int(today.year)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    gender=birthday_person["gender"]
    birth_year=int(birthday_person["year"])
    age_now=this_year-birth_year
    file_path = f"letter_templates/letter_1.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        contents = contents.replace("[EMAIL]", birthday_person["email"])
        contents = contents.replace("[PHONE]", str(birthday_person["phone"]))
        contents = contents.replace("[RELATION]", str(birthday_person["relation"]))
        contents = contents.replace("[AGE]", str(age_now))
        if gender=="male":
            contents = contents.replace("[GENDER1]", "HE")
            # contents = contents.replace("[GENDER2]", "his")
            contents = contents.replace("[GENDER3]", "him")

        else:
            contents = contents.replace("[GENDER1]", "SHE")
            # contents = contents.replace("[GENDER2]", "her")
            contents = contents.replace("[GENDER3]", "her")

        contents = contents.replace("[NO_OF_DOB]", str(age_now+1))



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="roysohag95@gmail.com",
            msg=f"Subject:Birthday Reminder!!\n\n{contents}"
        )

