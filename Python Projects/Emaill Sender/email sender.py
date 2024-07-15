from email.message import EmailMessage
import json
import ssl
import smtplib

# Open the JSON file with email credentials
with open('email_credentials.json', 'r') as file:
    email_credentials = json.load(file)

# Open the JSON file with email content
with open('email_content.json', 'r') as file:
    email_content = json.load(file)

email_sender = email_credentials["email_sender"]
email_password = email_credentials["email_password"]
email_reciever = email_credentials["email_reciever"]

email_subject = email_content["email_subject"]
email_body = email_content["email_body"]

email = EmailMessage()
email["From"] = email_sender
email["To"] = email_reciever
email["Subject"] = email_subject
email.set_content(email_body)

context = ssl.create_default_context()

# Correct the SMTP server hostname
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, email.as_string())