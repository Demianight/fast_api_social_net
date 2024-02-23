from email.mime.text import MIMEText
from smtplib import SMTP
from ssl import create_default_context

from pydantic import EmailStr

from config import settings


def send_mail(receiver: EmailStr, confirmation_code: str):
    message = MIMEText(settings.confirmation_url % confirmation_code)
    message['From'] = settings.email.username
    message['To'] = receiver
    message['Subject'] = 'Confirm your email'

    context = create_default_context()

    with SMTP(settings.email.host, settings.email.port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(settings.email.username, settings.email.password)
        server.send_message(message)
        server.quit()
