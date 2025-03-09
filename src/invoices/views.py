from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Invoice
from clients.models import Client
from accounts.models import User
from .forms import InvoiceForm  # Assume you've created a form for this

# List of invoices
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})

# Create a new invoice
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice created successfully!')
            return redirect('invoice_list')
    else:
        form = InvoiceForm()

    return render(request, 'invoices/invoice_form.html', {'form': form})

# View details of a specific invoice
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})

# Update an existing invoice
def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice updated successfully!')
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoices/invoice_form.html', {'form': form, 'invoice': invoice})

# Delete an invoice
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        messages.success(request, 'Invoice deleted successfully!')
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_confirm_delete.html', {'invoice': invoice})
