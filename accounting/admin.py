from django.contrib import admin

from accounting.models import Transactions


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id',
        'category',
        'organization',
        'info',
        'operation_type',
        'user',
        'update_date'
    )
