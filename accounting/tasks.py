from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.db.models import Sum, Q

from accounting.models import Transactions
from x1Lubeshko import settings
from x1Lubeshko.celery import app


@app.task(name="send_notification")
def send_notification():
    try:
        day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
        trans_objs = Transactions.objects.values('user__username', 'user__email').annotate(
            sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
            sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
        ).filter(date_operation__date=day_for_send)
        for trans_obj in trans_objs:
            subject = "Expense report"
            message = trans_obj
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [trans_obj.user__email]
            send_mail(subject, message, email_from, recipient_list)
        return None
    except Exception as e:
        print(e)


@app.task(name="send_notification2")
def send_notification2():
    print(datetime.utcnow())
