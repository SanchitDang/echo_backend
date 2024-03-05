from django.contrib import admin
from django.urls import path, include
from home.views import *
from apis import views
from apis.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('api/toggle_approval/<int:bid_id>/', toggle_approval, name='toggle-approval'),
    path('api/bids/<int:bid_id>/approval-status/', get_approval_status, name='get_approval_status'),

    # api urls
    path('api/users', views.UsersApiView.as_view()),
    path('api/getDashboardData/', DashboardDataAPIView.as_view(), name='dashboard-data'),
    path('api/bids', views.BidsApiView.as_view()),
    # path('api/products', views.ProductsApiVIew.as_view()),
    path('api/products/<str:user_id>', get_products, name='get_users_type'),
    path('api/products', add_product, name='add_product'),

    path('api/scraps', views.ScrapsApiVIew.as_view()),
    path('api/services', views.ServicessApiVIew.as_view()),
    path('api/bids/<int:id>/', views.BidsApiView.as_view()),
    path('api/users-by-type/', views.UsersByTypeApiView.as_view()),
    path('api/refers', views.RefersApiView.as_view()),
    path('api/categories/', ItemsCategoryListCreateView.as_view(), name='category-list-create'),
    path('api/subcategories/', ItemsSubCategoriesListCreateView.as_view(), name='subcategory-list-create'),
    path('api/subcategories/<int:category_id>/', ItemsSubCategoriesByCategoryView.as_view(), name='subcategory-by-category'), 
    path('api/assessment/', AssessmentApiView.as_view(), name='assessment'), 
    path('api/get_user_types_list/<int:user_id>', get_user_types_list, name='get_user_types_list'), 
    path('api/changeBidWinUser', changeBidWinUser, name='change-bid-win-user'), 
    path('api/referral/', referral, name='referral'),
    path('api/domains/', get_domains, name='get_domains'),
    path('api/users_types/', get_users_types, name='get_users_types'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
