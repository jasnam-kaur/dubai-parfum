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
    
from django.db import models

class Perfume(models.Model):
    # Choices for the dropdown in the admin/dashboard
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Unisex', 'Unisex'),
        ('Oud', 'Premium Oud'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='perfumes/')  # Images go to 'media/perfumes/'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
