import re
gmail_validation=r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_gmail=input("enter your email: ")
if re.search(gmail_validation, user_gmail):
    print("right email")
else:
    print("wrong email")