from django.contrib import admin

from accounting.models import Transactions, Card, CardBalance, Organization


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

@admin.register(CardBalance)
class CardBalanceAdmin(admin.ModelAdmin):
    list_display = (
        'card_balance_id',
        'card',
        'update_date',
        'sum_cur',

    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'organization_id',
        'organization_name',
        'update_date',

    )