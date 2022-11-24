import asyncio
import json
from datetime import datetime, timedelta
import dramatiq
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "x1Lubeshko.settings")
django.setup()
from celery import shared_task
from django.core.mail import send_mail
from django.db.models import Sum, Q

from accounting.models import Transactions, Card
from x1Lubeshko import settings
from x1Lubeshko.celery import app
from django.template import Template, Context
# from dramatiq.brokers.redis import RedisBroker
#
# redis_broker = RedisBroker(host="redis")
# dramatiq.set_broker(redis_broker)
#
#
# from celery.utils.log import get_task_logger
#
# logger = get_task_logger(__name__)
# @app.task
# def send_notification():
#     subject = "Expense report"
#     message = f"Ваш доход за прошлый день"
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['sergei_777@tut.by']
#     send_mail(subject, message, email_from, recipient_list)


# print(datetime.now())


# Card.objects.create(card_name='oopop', user_id=1)
# try:
#     day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
#     trans_objs = Transactions.objects.values('user__username', 'user__email').annotate(
#         sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
#         sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
#     ).filter(date_operation__date=day_for_send)
#     count = 1
#     Card.objects.create(card_name=str(count), user_id=1)
#     count = count + 1
#     for trans_obj in trans_objs:
#         subject = "Expense report"
#         message = f"Ваш доход за прошлый день {trans_obj['sum_income']}, а Ваши расходы составляют {trans_obj['sum_consumption']}"
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [trans_obj.get('user__email', None)]
#         send_mail(subject, message, email_from, recipient_list)
#     return None
# except Exception as e:
#     Card.objects.create(card_name='oopop', user_id=1)
#     print(e)


# @dramatiq.actor
# def send_notification2():
#     print(datetime.utcnow())
# if __name__ == '__main__':
#     send_notification.send()


import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

from decouple import config
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string


# @dramatiq.actor
async def send_mail_user(i):
    day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
    querysets = Transactions.objects.values('user__username', 'user__email').annotate(
        sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
        sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
    ).filter(date_operation__date=day_for_send)
    port = "587"
    smtp_server = "smtp.gmail.com"
    sender_email = "ittascompany2022@gmail.com"
    password = "bohsksyohssunujo"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'dsdsd'
    msg['From'] = sender_email
    msg['To'] = 'sergei_777@tut.by'
    msg['Reply-To'] = sender_email
    msg['Return-Path'] = sender_email

    # html = MIMEText(msg_html, 'html')
    # msg.attach(html)

    try:
        users_mail = ['sergei_777@tut.by']
        port = 587
        mail = smtplib.SMTP(smtp_server, port)
        context = ssl.create_default_context()
        mail.ehlo()
        mail.starttls(context=context)
        mail.ehlo()
        mail.login(sender_email, password)
        mail.sendmail(sender_email, users_mail, msg.as_string())
        # mail.quit()
        return True
    except (BadHeaderError, smtplib.SMTPAuthenticationError):
        return False
    # return redirect('password_reset_done')


if __name__ == '__main__':
    send_mail_user()

# from async_sender import Mail
# import asyncio
# def kk():
#     loop = asyncio.get_event_loop()
#
#     mail = Mail()
#
#     loop.run_until_complete(mail.send_message("Hello", from_address="from@example.com",
#                       to="to@example.com", body="Hello world!"))
