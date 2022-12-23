import smtplib, ssl
import ssl

host = "smtp.gmail.com"
port = 465


username = "pratoshb.othersubs@gmail.com"
password = "celsgdifitzyldwi"

receiver = "pratoshb.social@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi
Bye
How are you
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


