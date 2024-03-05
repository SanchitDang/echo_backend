from django.urls import path
from .import views

# admin creds for django panel
# admin@admin.com
# admin

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('panel-login/', views.panel_login, name='panel_login'),
    path('panel-logout/', views.panel_logout, name='panel_logout'),


    path('my-profile', views.my_profile, name='my_profile'),

    path('users-by-type/manufacturers', views.manufacturers_list, name='manufacturers-users-by-type'),
    path('users-by-type/suppliers', views.suppliers_list, name='suppliers-users-by-type'),
    path('users-by-type/service-provider', views.service_provider_list, name='service-provider-users-by-type'),

    path('user-profile/<int:id>/', views.edit_user_profile, name='user-profile'),
    path('user-assessment/<int:id>/', views.edit_user_assessment, name='user-assessment'),


    path('bids/', views.bids_view, name='bids-list'),
    path('bids_by_type/', views.bids_by_type_view, name='bids-by-type'),
    path('bids/edit-bid/<str:bid_id>/', views.bids_edit_view, name='edit-bid'),

    path('create_assessment/', views.create_assessment, name='create_assessment'),
    path('edit_assessment/<int:assessment_id>/', views.edit_assessment, name='edit_assessment'),


    path('category-list/', views.category_list, name='category_list'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:category_id>/', views.update_category, name='edit_category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),


    path('sub-category-list/', views.sub_category_list, name='sub_category_list'),
    path('add-sub-category/', views.add_sub_category, name='add_sub_category'),
    path('edit-sub-category/<int:sub_category_id>/', views.update_sub_category, name='edit_sub_category'),
    path('delete-sub-category/<int:id>/', views.delete_subcategory, name='delete_sub_category'),    


    path('user/products/<str:user_id>', views.view_product, name='user-products'),
    path('user/scrvices/<str:user_id>', views.view_scrvices, name='user-scrvices'),
    path('user/scraps/<str:user_id>', views.view_scrap, name='user-scrap'),
    path('referral-list/', views.referral_list, name='referral_list'),


    path('refers-list/', views.refers_list, name='refers_list'),
    path('referral/<int:referral_id>/', views.delete_referral, name='delete_referral'),


    path('manufacturers/<int:user_id>/bids-list/', views.manufacturer_bids_list, name='manufacturer_bids_list'),
    path('suppliers/<int:user_id>/bids-list/', views.supplier_bids_list, name='supplier_bids_list'),
    path('suppliers/<int:user_id>/<int:bid_id>/bids-view/', views.supplier_view_bid_details, name='supplier_bids_detail_view'),

    path('domains-list', views.domains_list, name='domains_list'),
    path('add-domani', views.add_domains, name='add_domains'),

    path('user_type_list', views.user_type_list, name='user_type_list'),
    path('add-user-type', views.add_user_type, name='add_user_type'),


]   