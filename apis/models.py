from django.db import models

# python manage.py makemigrations
# python manage.py migrate  

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)
    address = models.CharField(max_length=500, blank=True, null=True)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    company_size = models.CharField(max_length=500, blank=True, null=True)
    manufacturer_category = models.CharField(max_length=500, blank=True, null=True)
    adhaar_number = models.CharField(max_length=200, blank=True, null=True)

class Bids(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    party1_id = models.CharField(max_length=100)
    party1_name = models.CharField(max_length=100)
    party2_id = models.CharField(max_length=100, null=True)
    party2_name = models.CharField(max_length=100, null=True)

class Refers(models.Model):
    id = models.AutoField(primary_key=True)
