import re 

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
while True:
    user_email = input("Enter email :")

    if re.search(email_condition,user_email):
        print("Wright email")
        break
    else:
        print("Wrong email")