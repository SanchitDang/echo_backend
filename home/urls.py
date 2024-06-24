from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
# admin creds for django panel
# admin@admin.com
# admin

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('execution-dashboard', views.execution_dashboard, name='execution_dashboard'),
    path('service-support-dashboard', views.service_support_dashboard, name='service_support_dashboard'),
    path('freelancers-dashboard', views.freelancers_dashboard, name='freelancers_dashboard'),
    path('referral-dashboard', views.referral_dashboard, name='referral_dashboard'),

    path('panel-login', views.panel_login, name='panel_login'),
    path('panel-logout', views.panel_logout, name='panel_logout'),

    path('my-profile', views.my_profile, name='my_profile'),

    path('users-by-type/manufacturers', views.manufacturers_list, name='manufacturers-users-by-type'),
    path('users-by-type/suppliers', views.suppliers_list, name='suppliers-users-by-type'),
    path('users-by-type/service-provider', views.service_provider_list, name='service-provider-users-by-type'),

    path('user-profile/<int:id>/', views.edit_user_profile, name='user-profile'),
    path('delete-user/<int:id>/', views.delete_user, name='delete-user'),
    path('user-assessment/<int:id>/', views.edit_user_assessment, name='user-assessment'),


    path('bids/', views.bids_view, name='bids-list'),
    path('bids_by_type/', views.bids_by_type_view, name='bids-by-type'),
    path('bids/edit-bid/<str:bid_id>/', views.bids_edit_view, name='edit-bid'),
    path('bids/delete-bid/<str:bid_id>/', views.bids_delete_view, name='delete-bid'),
    path('bids/bid_approve_disapprove/<str:bid_id>/', views.bid_approve_disapprove, name='bid_approve_disapprove'),

    # path('create_assessment/', views.create_assessment, name='create_assessment'),
    # path('edit_assessment/<int:assessment_id>/', views.edit_assessment, name='edit_assessment'),


    path('category-list/', views.category_list, name='category_list'),
    path('add-category/', views.add_category, name='add_category'),
    path('category-approve-disapprove/<str:id>', views.category_approve_disapprove, name='category_approve_disapprove'),
    path('edit-category/<int:category_id>/', views.update_category, name='edit_category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),


    path('sub-category-list/', views.sub_category_list, name='sub_category_list'),
    path('subcategory-approve-disapprove/<str:id>', views.subcategory_approve_disapprove, name='subcategory_approve_disapprove'),
    path('add-sub-category/', views.add_sub_category, name='add_sub_category'),
    path('edit-sub-category/<int:sub_category_id>/', views.update_sub_category, name='edit_sub_category'),
    path('delete-sub-category/<int:id>/', views.delete_subcategory, name='delete_sub_category'),    


    path('user/products/<str:user_id>', views.view_product, name='user-products'),
    path('user/scrvices/<str:user_id>', views.view_scrvices, name='user-scrvices'),
    path('user/scraps/<str:user_id>', views.view_scrap, name='user-scrap'),
    path('referral-list/', views.referral_list, name='referral_list'),
    path('approve-disapprove-user/<int:user_id>/', views.approve_disapprove_user, name='approve_disapprove_user'),


    path('refers-list/', views.refers_list, name='refers_list'),
    path('referral/<int:referral_id>/', views.delete_referral, name='delete_referral'),


    path('manufacturers/<int:user_id>/bids-list/', views.manufacturer_bids_list, name='manufacturer_bids_list'),
    path('suppliers/<int:user_id>/bids-list/', views.supplier_bids_list, name='supplier_bids_list'),
    path('suppliers/<int:user_id>/<int:bid_id>/bids-view/', views.supplier_view_bid_details, name='supplier_bids_detail_view'),

    path('domains-list', views.domains_list, name='domains_list'),
    path('add-domani', views.add_domains, name='add_domains'),
    path('domain-approve-disapprove/<str:id>', views.domain_approve_disapprove, name='domain_approve_disapprove'),


    path('products-list', views.products_list, name='products_list'),
    path('edit-products/<str:id>', views.edit_product, name='edit_product'),
    path('delete-product<str:id>', views.delete_product, name='delete_product'),
    path('product-approve-disapprove/<str:id>', views.product_approve_disapprove, name='product_approve_disapprove'),


    path('assement-list', views.assement_list, name='assement_list'),
    path('usertype-approve-disapprove/<str:id>', views.user_approve_disapprove, name='user_approve_disapprove'),
    path('delete-assessment/<str:id>', views.delete_assessment, name='delete_assessment'),

    path('user_type_list', views.user_type_list, name='user_type_list'),
    path('add-user-type', views.add_user_type, name='add_user_type'),


    path('banner-list', views.banner_list, name='banner_list'),
    path('add-banner', views.add_banner, name='add_banner'),
    path('update-banner/<str:id>', views.update_banner, name='update_banner'),
    path('delete-banner/<str:id>', views.delete_banner, name='delete_banner'),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)