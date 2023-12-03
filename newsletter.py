import smtplib
import ssl
import os

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

gmail_address = os.getenv("GMAIL_ADDRESS")
gmail_password = os.getenv("GMAIL_PASSWORD")

email = EmailMessage()

email['Subject'] = "Test"
email["From"] = gmail_address

with open("newsletter_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

email.add_alternative(html_content, subtype="html")

with open("emails.txt", "r") as file:
    subscriber_email_addresses = [line.strip() for line in file]

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
    smtp_server.login(gmail_address, gmail_password)

    for subsciber_email_address in subscriber_email_addresses:
        email["To"] = subsciber_email_address

        smtp_server.send_message(email)