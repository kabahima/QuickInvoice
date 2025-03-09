from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'user', 'invoice_number', 'amount', 'issue_date', 'due_date', 'status']
