from django.urls import path

from accounting.views.balance_views import BalanceList, BalanceCreate
from accounting.views.categories_views import CategoryCreate, CategoryList, CategoryDetail
from accounting.views.organization_views import OrganizationListCreate, OrganizationRUD
from accounting.views.transaction_views import TransactionCreate, TransactionDelete, TransactionUpdate, TransactionList

urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),
    path('category/list/', CategoryList.as_view(), name='category-list'),
    path('category/detail/<int:category_id>', CategoryDetail.as_view()),

    path('organization/list-create/', OrganizationListCreate.as_view()),
    path('organization/rud/<int:org_id>', OrganizationRUD.as_view()),

    path('transaction/create/', TransactionCreate.as_view()),
    path('transaction/list/', TransactionList.as_view()),
    path('transaction/delete/<int:transaction_id>', TransactionDelete.as_view()),
    path('transaction/update/<int:transaction_id>', TransactionUpdate.as_view()),

    path('balance/list/', BalanceList.as_view()),
    path('balance/create/', BalanceCreate.as_view()),
    # path('balance/stat/', BalanceStat.as_view()),

]
