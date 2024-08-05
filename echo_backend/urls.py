from django.contrib import admin
from django.urls import path, include
from home.views import *
from apis import views
from apis.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('master-admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('admin/', include('home.urls')),

    path('api/users', views.UsersApiView.as_view()),
    path('api/scraps', views.ScrapsApiVIew.as_view()),
    path('api/services', views.ServicessApiVIew.as_view()),

    path('api/toggle_approval/<int:bid_id>/', toggle_approval, name='toggle-approval'),
    path('api/toggle_user_approval/<int:user_id>/', toggle_user_approval, name='user-toggle-approval'),
    path('api/bids/<int:bid_id>/approval-status/', get_approval_status, name='get_approval_status'),
    path('api/toggle_user_assessment_approval/<str:assessment_id>/', toggle_user_assessment_approval, name='toggle_user_assessment_approval'),
    path('api/toggle-product-approval/<str:product_id>/', toggle_product_approval, name='toggle-product-approval'),

    path('api/getDashboardData/', DashboardDataAPIView.as_view(), name='dashboard-data'),
    
    path('api/products/<str:user_id>', get_products, name='get_products'),
    path('api/products', add_product, name='add_product'),

    path('api/bids', views.BidsApiView.as_view()),
    path('api/bids/<int:id>/', views.BidsApiView.as_view()),
    path('api/changeBidWinUser', changeBidWinUser, name='change-bid-win-user'), 
        
    path('api/assessment/', AssessmentApiView.as_view(), name='assessment'), 

    path('api/referral/', referral, name='referral'),

    path('api/refers', views.RefersApiView.as_view()),
    
    path('api/categories/', ItemsCategoryListCreateView.as_view(), name='category-list-create'),
    path('api/subcategories/', ItemsSubCategoriesListCreateView.as_view(), name='subcategory-list-create'),
    path('api/subcategories/<int:category_id>/', ItemsSubCategoriesByCategoryView.as_view(), name='subcategory-by-category'), 

    path('api/users_types/', get_users_types, name='get_users_types'),
    path('api/users-by-type/', views.UsersByTypeApiView.as_view()),
    path('api/get_user_types_list/<int:user_id>', get_user_types_list, name='get_user_types_list'), 
    path('api/get-approve-users-types', get_approve_users_types, name='get_approve_users_types'),

    path('api/get-units/', get_units, name='get_units'),

    path('api/get-approve-categories/', get_approve_categories, name='get_approve_categories'),
    path('api/get-approve-subcategories/<int:category_id>/', get_approve_subcategories, name='get_approve_subcategories'),

    path('api/get-approve-users', get_approve_users, name='get_approve_users'),
    path('api/get-unapprove-users', get_unapprove_users, name='get_unapprove_users'),

    path('api/domains/', get_domains, name='get_domains'),
    path('api/get-approved-domains', get_approved_domains, name='get_approved_domains'),
    path('api/get-unapproved-domains', get_unapproved_domains, name='get_unapproved_domains'),

    path('api/get-approved-products', get_approved_products, name='get_approved_products'),
    path('api/get-unapproved-products', get_unapproved_products, name='get_unapproved_products'),

    path('api/get-banner', get_banner, name='get_banner'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
