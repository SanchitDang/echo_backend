from rest_framework import serializers
from .models import *
from home.models import Assessments

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ScrapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraps
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


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



class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'



class AssessmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessments
        fields = '__all__'


