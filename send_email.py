import smtplib, ssl
import os
import decouple

pw = decouple.config('PASSWORD')

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pratoshb.othersubs@gmail.com"
    password = pw

    receiver = "pratoshb.social@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
