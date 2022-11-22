import json
from datetime import datetime, timedelta


from django.core.mail import send_mail
from django.db.models import Sum, Q

from accounting.models import Transactions, Card
from x1Lubeshko import settings
from x1Lubeshko.celery import app
from django.template import Template, Context


@app.task
async def send_notification():
    try:
        day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
        trans_objs = Transactions.objects.values('user__username', 'user__email').annotate(
            sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
            sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
        ).filter(date_operation__date=day_for_send)
        async for trans_obj in trans_objs:
            subject = "Expense report"
            message = f"Ваш доход за прошлый день {trans_obj['sum_income']}, а Ваши расходы составляют {trans_obj['sum_consumption']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [trans_obj.get('user__email', None)]
            count = 1
            Card.objects.create(card_name=str(count))
            print('ioioiioioi')
            await send_mail(subject, message, email_from, recipient_list)
            count = count + 1
        return None
    except Exception as e:
        print(e)


# @dramatiq.actor
# def send_notification2():
#     print(datetime.utcnow())
if __name__ == '__main__':
    send_notification.send()