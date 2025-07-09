from django.urls import path
from . import views

urlpatterns = [
    path('transaction/', views.transaction, name='transaction'),
    path('invoices/', views.invoices, name='invoices'),
    path('expenses/', views.expenses, name='expenses'),
    path('income/', views.income, name='income'),
    path('tax-reports/', views.tax_reports, name='tax_reports'),
    path('salary-payments/', views.salary_payments, name='salary_payments'),
    path('financial-reports/', views.financial_reports, name='financial_reports'),
    # Add more finance-related paths here as needed

]