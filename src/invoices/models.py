from django.db import models
from src.clients.models import Client  # Assuming you have a 'clients' app
from src.accounts.models import User  # Assuming 'User' model is in the 'accounts' app

class Invoice(models.Model):
    # Choices for invoice status
    PENDING = 'Pending'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
    ]
    
    # Fields
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')  # Link to account (user)
    invoice_number = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.client.company_name}"

    class Meta:
        ordering = ['-issue_date']
