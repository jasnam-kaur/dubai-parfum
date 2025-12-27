from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Role Choices
    ADMIN = 'ADMIN'   # You (Technical)
    OWNER = 'OWNER'   # Dubai Parfum Business Owner
    CLIENT = 'CLIENT' # Business/Wholesale Customers
    
    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (OWNER, 'Business Owner'),
        (CLIENT, 'Business Client'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"