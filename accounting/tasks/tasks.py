import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "x1Lubeshko.settings")

import django
django.setup()

from datetime import datetime, timedelta

import dramatiq as dramatiq
from django.core.mail import send_mail
from django.db.models import Sum, Q

from accounting.models import Transactions
from x1Lubeshko import settings
from x1Lubeshko.celery import app
from django.template import Template, Context


@dramatiq.actor
def send_notification():
    try:
        day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
        trans_objs = Transactions.objects.values('user__username', 'user__email').annotate(
            sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
            sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
        ).filter(date_operation__date=day_for_send)
        for trans_obj in trans_objs:
            subject = "Expense report"
            message = f"Ваш доход за прошлый день {trans_obj['sum_income']}, а Ваши расходы составляют {trans_obj['sum_consumption']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [trans_obj.get('user__email', None)]
            send_mail(subject, message, email_from, recipient_list)
        return None
    except Exception as e:
        print(e)


# @dramatiq.actor
# def send_notification2():
#     print(datetime.utcnow())
if __name__ == '__main__':
    send_notification.send()