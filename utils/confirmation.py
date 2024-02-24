from email.mime.text import MIMEText
from smtplib import SMTP
from ssl import create_default_context

from pydantic import EmailStr

from config import settings


def send_mail(receiver: EmailStr, confirmation_code: str):
    message = MIMEText(settings.confirmation_url % confirmation_code)
    message['From'] = settings.mail.username
    message['To'] = receiver
    message['Subject'] = 'Confirm your mail'

    context = create_default_context()

    with SMTP(settings.mail.host, settings.mail.port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(settings.mail.username, settings.mail.password)
        server.send_message(message)
        server.quit()
