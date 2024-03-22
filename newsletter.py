import smtplib
import ssl
import os

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

gmail_address = os.getenv("GMAIL_ADDRESS")
gmail_password = os.getenv("GMAIL_PASSWORD")

with open("newsletter_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

with open("emails.txt", "r") as file:
    subscriber_email_addresses = [line.strip() for line in file]

for subscriber_email_address in subscriber_email_addresses:
    email = EmailMessage()
    email['Subject'] = "Test"
    email["From"] = gmail_address
    email["To"] = subscriber_email_address
    email.set_content(html_content, subtype="html")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
            smtp_server.login(gmail_address, gmail_password)
            smtp_server.send_message(email)
        print(f"Email sent successfully to {subscriber_email_address}")
    except Exception as e:
        print(f"Failed to send email to {subscriber_email_address}. Error: {e}")
