import pytz
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand


from accounting.tasks import send_notification2


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Preparing scheduler'))
        scheduler = BlockingScheduler(timezone=pytz.UTC)
        # every_day_at_05_05_utc = CronTrigger('* * * * *')
        scheduler.add_job(send_notification2, 'cron', day_of_week='mon-sun', hour=22, minute=15,)
        self.stdout.write(self.style.NOTICE('Start scheduler'))
        scheduler.start()
