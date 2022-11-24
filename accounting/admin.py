from django.contrib import admin

from accounting.models import Transactions, Card, Organization


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


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'card_id',
        'card_name',
        'beg_balance',
        'user',
        'update_date'
    )

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'organization_id',
        'organization_name',
        'update_date',

    )