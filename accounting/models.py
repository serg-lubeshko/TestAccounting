from django.db import models

from users.models import MyUser


class Common(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Юзер')
    update_date = models.DateTimeField(verbose_name='Последние изменения', auto_now=True)

    class Meta:
        abstract = True


class Category(Common):
    category_id = models.BigAutoField(primary_key=True, verbose_name="id")
    category_name = models.CharField(max_length=255, verbose_name="Название категории")

    # code = models.ForeignKey(Code, on_delete=models.PROTECT, verbose_name="Шифр товара")
    # category_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'сategory'
        verbose_name = 'Категория | Category'
        verbose_name_plural = 'Категории | Category'

    def __str__(self):
        return self.category_name


class Organization(Common):
    organization_id = models.BigAutoField(primary_key=True, verbose_name="id")
    organization_name = models.CharField(max_length=255, verbose_name="Название организации")

    class Meta:
        db_table = 'organization'
        verbose_name = 'Организация | Organization'
        verbose_name_plural = 'Организации | Organization'

    def __str__(self):
        return self.organization_name


class Card(Common):
    card_id = models.BigAutoField(primary_key=True, verbose_name="id")
    card_name = models.CharField(max_length=255, verbose_name="Название карты")
    beg_balance = models.DecimalField(max_digits=20,
                                      decimal_places=2,
                                      verbose_name="Начальный баланс",
                                      default=0)

    class Meta:
        db_table = 'card'
        verbose_name = 'Карта | Card'
        verbose_name_plural = 'Карты | Card'

    def __str__(self):
        return self.card_name


class CardBalance(models.Model):
    card_balance_id = models.BigAutoField(primary_key=True, verbose_name="id")
    card = models.OneToOneField(Card, on_delete=models.CASCADE, related_name='card')
    update_date = models.DateTimeField(verbose_name='Последние изменения', auto_now=True)
    sum_cur = models.DecimalField(max_digits=20,
                                  decimal_places=2,
                                  verbose_name="Текущий баланс",
                                  default=0)

    class Meta:
        db_table = 'card_balance'
        verbose_name = 'Баланс | CardBalance'
        verbose_name_plural = 'Балансы | CardBalance'

    def __str__(self):
        return self.card


class Transactions(Common):
    OPERATION_TYPE = [
        (1, 'Доход'),
        (2, 'Расход')
    ]
    transaction_id = models.BigAutoField(primary_key=True, verbose_name="id")
    transaction_summ = models.DecimalField(max_digits=20,
                                           decimal_places=2,
                                           verbose_name="Сумма транзакции",
                                           default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация")
    info = models.CharField(max_length=500, verbose_name="Описание", blank=True, null=True)
    operation_type = models.IntegerField(choices=OPERATION_TYPE,
                                         verbose_name='Тип операции',
                                         null=True)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    date_operation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Транзакция | Transactions'
        verbose_name_plural = 'Транзакции | Transactions'

    def __str__(self):
        return f"{self.category} - {self.transaction_summ}"
