from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'password', 'username', 'user_type', 'address', 'company_name', 'company_size', 'manufacturer_category', 'adhaar_number']

class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids
        fields = '__all__'

class RefersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refers
        fields = '__all__'

class ItemsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsCategory
        fields = '__all__'

class ItemsSubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsSubCategories
        fields = '__all__'