import asyncio
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import BadHeaderError, send_mail


async def send_mail_user(item):
    smtp_server = "smtp.gmail.com"
    sender_email = "You_email@gmail.com"
    password = "password"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Баланс за вчерашний день)'
    msg['From'] = sender_email
    msg['To'] = item['user__email']
    message = f"Ваш доход за прошлый день {item['sum_income']}, а Ваши расходы составляют {item['sum_consumption']}"
    msg.attach(MIMEText(message, 'plain'))
    try:
        users_mail = [item['user__email']]
        port = 587
        mail = smtplib.SMTP(smtp_server, port)
        context = ssl.create_default_context()
        mail.ehlo()
        mail.starttls(context=context)
        mail.ehlo()
        mail.login(sender_email, password)
        mail.sendmail(sender_email, users_mail, msg.as_string())
        send_mail(sender_email, users_mail, msg.as_string())
        mail.quit()
        return True
    except (BadHeaderError, smtplib.SMTPAuthenticationError):
        return False

async def send_mail_default_django(item):
    subject = 'BALANCE'
    message = f"Ваш доход за прошлый день {item['sum_income']}, а Ваши расходы составляют {item['sum_consumption']}"
    email_from = "default_company@mail.ru"
    recipient_list = [item['user__email']]
    # await asyncio.sleep(1)
    send_mail(subject, message, email_from, recipient_list)


