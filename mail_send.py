import smtplib as s

email = input("Enter gmail:")
password = input("Enter password:")
subject = input("Enter subject :")
body = input("Enter body:")

ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login(email,password)

message = f"Subject:{subject}\n\n{body}"
listsend_to = []         #enter any no of gmail to send mail.

ob.sendmail(email,listsend_to,message)
ob.quit()