from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounting.models import Card, CardBalance, Transactions


@receiver(post_save, sender=Card)
def create_balance(sender, instance, created, **kwargs):
    print(instance)
    if created:
        print('create card')
        CardBalance.objects.create(
            card=instance,
            sum_cur=instance.beg_balance
        )


@receiver(post_save, sender=Transactions)
def change_balance(sender, instance, **kwargs):
    print(instance.transaction_summ)
    obj = CardBalance.objects.get(card=instance.card)
    obj.sum_cur = F('sum_cur') + instance.transaction_summ
    obj.save()
