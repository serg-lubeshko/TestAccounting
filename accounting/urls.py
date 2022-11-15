from django.urls import path

from accounting.views.categories_views import CategoryCreate, CategoryList, CategoryDetail
from accounting.views.organization_views import OrganizationListCreate, OrganizationRUD
from accounting.views.transaction_views import TransactionCreate

urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),
    path('category/list/', CategoryList.as_view()),
    path('category/detail/<int:category_id>', CategoryDetail.as_view()),

    path('organization/list-create/', OrganizationListCreate.as_view()),
    path('organization/rud/<int:org_id>', OrganizationRUD.as_view()),

    path('transaction/create/', TransactionCreate.as_view())

]
