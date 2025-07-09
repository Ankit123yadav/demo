from django.shortcuts import render


# Create your views here.

def transaction(request):
    return render(request, 'finance/templates/transaction.html')
# Add @login_required to all views here when implemented
def invoices(request):
    return render(request, 'finance/templates/invoices.html')
def expenses(request):
    return render(request, 'finance/templates/expenses.html')

def income(request):
    return render(request, 'finance/templates/income.html')

def tax_reports(request):
    return render(request, 'finance/templates/tax_reports.html')

def salary_payments(request):
    return render(request, 'finance/templates/salary_payments.html')

def financial_reports(request):
    return render(request, 'finance/templates/financial_reports.html')