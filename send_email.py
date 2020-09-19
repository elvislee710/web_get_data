import ssl
import smtplib, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_out_email(password):
    subject = 'An email with attachment from automate'
    body = 'This is an email with attachment sent from robot'
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = "testingballot@gmail.com"
    receiver_email = 'alanlee@futu5.com'
    context = ssl.create_default_context()
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message['Bcc'] = receiver_email

    message.attach(MIMEText(body, 'plain'))

    filename = 'last_trade_day.txt'

    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "content-Disposition",
        f"attachment;filename={filename}",
    )

    message.attach(part)
    text=message.as_string()

    # message = """Subject: Testing sending email to yourself\n
    #
    # {content}  This message is sent from py."""

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
