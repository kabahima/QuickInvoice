from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model to store information related to individual users or companies.
    Inherits from Django's AbstractUser.
    """
    ROLE_CHOICES = [
        ('individual', 'Individual'), 
        ('company', 'Company'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='individual')
    phone_number = models.CharField(max_length=15, blank=True, null=True) 
    address = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
    )

    def __str__(self):
        return self.username

