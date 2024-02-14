from django.contrib import admin
from django.urls import path
from home.views import *
from apis import views
from apis.views import *

# admin creds for django panel
# admin@admin.com
# admin

urlpatterns = [
    # web views urls
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('users_by_type/', users_by_type_view, name='users-by-type'),
    path('bids/', bids_view, name='bids'),
    path('bids_by_type/', bids_by_type_view, name='bids-by-type'),


    # api urls
    path('api/users', views.UsersApiView.as_view()),
    path('getDashboardData/', DashboardDataAPIView.as_view(), name='dashboard-data'),
    path('api/bids', views.BidsApiView.as_view()),
    path('api/bids/<int:id>/', views.BidsApiView.as_view()),
    path('api/users-by-type/', views.UsersByTypeApiView.as_view()),
    path('api/refers', views.RefersApiView.as_view()),
    path('api/categories/', ItemsCategoryListCreateView.as_view(), name='category-list-create'),
    path('api/subcategories/', ItemsSubCategoriesListCreateView.as_view(), name='subcategory-list-create'),
    path('api/subcategories/<int:category_id>/', ItemsSubCategoriesByCategoryView.as_view(), name='subcategory-by-category'),   

]
