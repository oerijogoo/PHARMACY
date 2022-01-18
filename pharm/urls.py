from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='pharm-index'),
    path('drugs/', views.drugs, name='pharm-drugs'),
    path('drugs/delete/<int:pk>/', views.drug_delete,
         name='pharm-drugs-delete'),
    path('drugs/detail/<int:pk>/', views.drug_detail,
         name='pharm-drugs-detail'),
    path('drugs/edit/<int:pk>/', views.drug_edit,
         name='pharm-drugs-edit'),
    path('customers/', views.customers, name='pharm-customers'),
    path('customers/detail/<int:pk>/', views.customer_detail,
         name='pharm-customer-detail'),
    path('order/', views.order, name='pharm-order'),
]
