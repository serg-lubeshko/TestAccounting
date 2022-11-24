import asyncio
import threading
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BlockingScheduler
from django.core.management.base import BaseCommand
from django.db.models import Sum, Q

from accounting.models import Transactions
from accounting.tasks import send_mail_user, kk


# async print_current_date():
# print(datetime.now())
# for i in range(15):
#     time.sleep(5)
#     print(i)


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()
def vv():
    threads=[]
    thread = threading.Thread(target=send_mail_user)
    thread.start()
    threads.append(thread)


def main_func_send():
    # day_for_send = (datetime.utcnow() - timedelta(days=1)).date()
    # querysets = Transactions.objects.values('user__username', 'user__email').annotate(
    #     sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
    #     sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
    # ).filter(date_operation__date=day_for_send)
    loop = get_or_create_eventloop()
    print(loop)
    tasks = [send_mail_user(i) for i in range(15)]
    loop.run_until_complete(asyncio.gather(*tasks))





class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Preparing scheduler'))
        scheduler = BlockingScheduler(timezone=pytz.UTC)
        # every_day_at_05_05_utc = CronTrigger('* * * * *')
        scheduler.add_job(
            main_func_send,
            'cron', day_of_week='mon-sun', hour='*', minute='*',
            # CronTrigger.from_crontab("* * * * *")
        )
        self.stdout.write(self.style.NOTICE('Start scheduler'))
        scheduler.start()
