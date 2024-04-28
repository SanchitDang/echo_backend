from django.db import models

# python manage.py makemigrations
# python manage.py migrate 


# application users
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200) # current user type selected by user
    user_types = models.JSONField(default=list) 
    address = models.CharField(max_length=500, blank=True, null=True)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    company_size = models.CharField(max_length=500, blank=True, null=True)
    manufacturer_category = models.CharField(max_length=500, blank=True, null=True)
    adhaar_number = models.CharField(max_length=200, blank=True, null=True)
    is_approved = models.CharField(max_length=5, default="no", blank=True, null=True)

    def __str__(self):
        return self.username 

class Bids(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    party1_id = models.CharField(max_length=100)
    party1_name = models.CharField(max_length=100)
    party2_id = models.CharField(max_length=100, default="x")
    party2_name = models.CharField(max_length=100, default="x")
    reffered_by_id = models.CharField(max_length=200, null=True)
    reffered_by_name = models.CharField(max_length=200, null=True)
    other_parties = models.TextField(default="[]")
    bid_category = models.CharField(max_length=100, null=True)
    bid_sub_category = models.CharField(max_length=100, null=True)
    bid_type = models.CharField(max_length=10, null=True)               #one_time or real_time
    bid_win_type = models.CharField(max_length=10, null=True)           #highest win or lowest win
    bid_status= models.CharField(max_length=20, null=True)           #on_going cancelled or finished
    bid_opening_time = models.TextField(default='2000-01-01T18:18', null=True)
    bid_closing_time = models.TextField(default='2000-01-01T18:18', null=True)
    is_approved = models.CharField(max_length=5, default="no")
    bid_quantity = models.CharField(max_length=20, null=True)
    bid_delivery_time = models.CharField(max_length=20, null=True)
    bid_material = models.CharField(max_length=20, null=True)
    percentage_inc_dec = models.CharField(max_length=20, null=True)
    img = models.FileField(blank=True, null=True, default="")





class Products(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(max_length=1000,blank=True, null=True)
    user_id = models.CharField(max_length=10,blank=True, null=True)
    item_type = models.CharField(max_length=100,blank=True, null=True)
    item_price = models.CharField(max_length=100,blank=True, null=True)
    item_availability = models.CharField(max_length=100,blank=True, null=True)
    item_category = models.CharField(max_length=100,blank=True, null=True)
    item_sub_category = models.CharField(max_length=100,blank=True, null=True)
    img = models.FileField(blank=True, null=True)
    is_approved = models.CharField(max_length=10, blank=True, null=True)



class Services(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=10)

class Scraps(models.Model):
    
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=10)
    item_type = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)


class Refers(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer_id = models.CharField(max_length=200, null=True)
    manufacturer_username = models.CharField(max_length=200, null=True)
    seller_id = models.CharField(max_length=200, null=True)
    seller_username = models.CharField(max_length=200, null=True)
    referral_price = models.CharField(max_length=20, null=True)
    reffered_by_id = models.CharField(max_length=10, null=True)
    reffered_by_username = models.CharField(max_length=200, null=True)
    reffered_req_id = models.CharField(max_length=200, default = '')


class ItemsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200, null=True)
    is_approved = models.CharField(max_length=5, default="no", blank=True, null=True)

    def __str__(self) :
        return self.category

class ItemsSubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    sub_category = models.CharField(max_length=200, null=True)
    category_id = models.CharField(max_length=200, null=True)
    is_approved = models.CharField(max_length=5, default="no", blank=True, null=True)

    def __str__(self) :
        return self.sub_category


class Domains(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)  
    is_approved = models.CharField(max_length=5, default="no", blank=True, null=True)
    

class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True) 
    is_approved = models.CharField(max_length=5, default="no", blank=True, null=True)


class Assessment(models.Model):
    data = models.JSONField(default=dict)

    def __str__(self):
        return f"Assessment {self.pk}"


