from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'password', 'username', 'user_type', 'address', 'company_name', 'company_size', 'manufacturer_category', 'adhaar_number']

class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids
        fields = ['id', 'item', 'price', 'description', 'party1_id', 'party1_name', 'party2_id', 'party2_name']

class RefersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refers
        fields = ['id', 'manufacturer_id', 'manufacturer_username', 'seller_id', 'seller_username', 'referral_price']