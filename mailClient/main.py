# Client Mail Server

import email.mime.multipart
import smtplib
from smtplib import SMTP
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def generate_mail():
    server = SMTP('smtp.gmail.com', 587)
    # start server
    server.ehlo()
    server.starttls()

# with open('password.txt', 'r') as f:
    # password = f.read()
    server.login('mvpshaggy@gmail.com', 'Password')
    mail_msg = MIMEMultipart()
    mail_msg['From'] = 'biostar'
    mail_msg['To'] = 'raghavmarwaha1998@gmail.com'
    mail_msg['Subject'] = "Test email from smtp client"

    with open('message.txt', 'r') as bod:
        message_body = bod.read()
    mail_msg.attach(MIMEText(message_body, 'plain'))

# functionality for attachments
    file = 'keylogger.PNG'
    attachment = open(file, 'rb')

    payload = MIMEBase('image', 'png')
    payload.set_payload(attachment.read())

    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=file)
    mail_msg.attach(payload)

    text = mail_msg.as_string()
    server.sendmail('mvpshaggy@gmail.com', 'raghavmarwaha1998@gmail.com', text)
    attachment.close()


generate_mail()






