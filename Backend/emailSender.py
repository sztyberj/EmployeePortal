import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logPassGenerator import *


def Sender(reciver_address, subject, mail_content):

    # ========= Email and Password Config  ========= #
    sender_email = 'employeeportal.no.reply@gmail.com'
    password = 'Test12345678'

    # ========= Setup MIME  ========= #

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciver_address
    message['Subject'] = subject

    message.attach(MIMEText(mail_content, 'plain'))

    # ========= Create SMT Session  ========= #

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, password)
    text = message.as_string()
    session.sendmail(sender_email, reciver_address, text)
    session.quit()
    print('Mail Send')

