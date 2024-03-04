from django.contrib import admin
from .models import Users,ItemsCategory,ItemsSubCategories,Bids,Referral
# Register your models here.




admin.site.register(Users)
admin.site.register(ItemsCategory)
admin.site.register(ItemsSubCategories)
admin.site.register(Bids)
admin.site.register(Referral)
