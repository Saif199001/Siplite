from django.db import models

# Create your models here.
class BillingAddress(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)