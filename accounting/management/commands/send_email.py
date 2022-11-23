import pytz
from apscheduler.schedulers.background import BlockingScheduler
from django.core.management.base import BaseCommand
from apscheduler.triggers.cron import CronTrigger
from accounting.tasks import send_notification


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Preparing scheduler'))
        scheduler = BlockingScheduler(timezone=pytz.UTC)
        # every_day_at_05_05_utc = CronTrigger('* * * * *')
        scheduler.add_job(
            send_notification.send,
            'cron', day_of_week='mon-sun', hour='*', minute='*',
            # CronTrigger.from_crontab("* * * * *")
        )
        self.stdout.write(self.style.NOTICE('Start scheduler'))
        scheduler.start()
