from django.db import models

from users.models import MyUser


class Common(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Юзер')
    update_date = models.DateTimeField(verbose_name='Последние изменения', auto_now=True)

    class Meta:
        abstract = True


class Category(Common):
    """
    Транзакция должна содержать в себе: сумму\*, время\*, категорию\*, организацию\*, описание.

    """
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
