# Client Mail Server

import email.mime.multipart
import smtplib
from smtplib import SMTP
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from encrypter import CryptoEngine
from pathlib import Path


def generate_mail():
    server = SMTP('smtp.gmail.com', 587)
    # start server
    server.ehlo()
    server.starttls()

    # Secret encryption and decryption

    # Secret input and encryption
    password = input("Enter your password! : ")
    encrypter = CryptoEngine(password)
    encrypter.encrypt_message()

    # Secret decryption
    decrypter = CryptoEngine(password)
    credential_password = decrypter.decrypt_message()

    # generate email
    server.login('mvpshaggy@gmail.com', credential_password)
    mail_msg = MIMEMultipart()
    mail_msg['From'] = 'biostar'
    mail_msg['To'] = 'raghavmarwaha1998@gmail.com'
    mail_msg['Subject'] = "Test email from smtp client"
    # write body to file
    with open('message.txt', 'r') as bod:
        message_body = bod.read()
    mail_msg.attach(MIMEText(message_body, 'plain'))

# functionality for attachments
    file = 'keylogger.PNG'
    attachment = open(file, 'rb')
# generate payload for attachment
    payload = MIMEBase('image', 'png')
    payload.set_payload(attachment.read())

# encode payload and attach with header and body MIME
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=file)
    mail_msg.attach(payload)

# convert the message to string and send email
    text = mail_msg.as_string()
    server.sendmail('mvpshaggy@gmail.com', 'raghavmarwaha1998@gmail.com', text)
    attachment.close()

# function call


generate_mail()






