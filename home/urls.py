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

    path('bids/', views.bids_view, name='bids-list'),
    path('bids-one-time/', views.bids_view_one, name='bids-list-one-time'),
    path('bids-real-time/', views.bids_view_real, name='bids-list-real-time'),
    path('bids_by_type/', views.bids_by_type_view, name='bids-by-type'),
    path('bids/edit-bid/<str:bid_id>/', views.bids_edit_view, name='edit-bid'),
    path('bids/delete-bid/<str:bid_id>/', views.bids_delete_view, name='delete-bid'),
    path('bids/bid_approve_disapprove/<str:bid_id>/', views.bid_approve_disapprove, name='bid_approve_disapprove'),

    path('units-list/', views.units_list, name='units_list'),
    path('add-units/', views.add_unit, name='add_units'),
    path('edit-units/<int:units_id>/', views.update_unit, name='edit_units'),
    path('delete-units/<int:units_id>/', views.delete_unit, name='delete_units'),

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
    path('delete-domanin/<int:id>', views.delete_domains, name='delete_domain'),
    path('domain-approve-disapprove/<str:id>', views.domain_approve_disapprove, name='domain_approve_disapprove'),


    path('products-list', views.products_list, name='products_list'),
    path('edit-products/<str:id>', views.edit_product, name='edit_product'),
    path('delete-product<str:id>', views.delete_product, name='delete_product'),
    path('product-approve-disapprove/<str:id>', views.product_approve_disapprove, name='product_approve_disapprove'),


    path('assement-list', views.assement_list, name='assement_list'),
    path('usertype-approve-disapprove/<str:id>', views.user_approve_disapprove, name='user_approve_disapprove'),
    path('user-assessment/<int:id>/', views.edit_user_assessment, name='user-assessment'),
    path('delete-assessment/<str:id>', views.delete_assessment, name='delete_assessment'),

    path('user_type_list', views.user_type_list, name='user_type_list'),
    path('add-user-type', views.add_user_type, name='add_user_type'),


    path('banner-list', views.banner_list, name='banner_list'),
    path('add-banner', views.add_banner, name='add_banner'),
    path('update-banner/<str:id>', views.update_banner, name='update_banner'),
    path('delete-banner/<str:id>', views.delete_banner, name='delete_banner'),

    # Download as excel file
    path('export-to-excel-suppliers/', views.export_to_excel_sup, name='export-to-excel-suppliers'),
    path('export-to-excel-manufacturers/', views.export_to_excel_man, name='export-to-excel-manufacturers'),
    path('export-to-excel-service-providers/', views.export_to_excel_service, name='export-to-excel-service-providers'),
    path('export-to-excel-referrals/', views.export_to_excel_referrals, name='export-to-excel-referrals'),
    path('export-to-excel-refers/', views.export_to_excel_refers, name='export-to-excel-refers'),
    path('export-to-excel-one-time-bids/', views.export_to_excel_one_time, name='export-to-excel-one-time-bids'),
    path('export-to-excel-real-time-bids/', views.export_to_excel_real_time, name='export-to-excel-real-time-bids'),
    path('export-to-excel-categories/', views.export_to_excel_cat, name='export-to-excel-categories'),
    path('export-to-excel-sub-categories/', views.export_to_excel_sub_cat, name='export-to-excel-sub-categories'),
    path('export-to-excel-products/', views.export_to_excel_products, name='export-to-excel-products'),
    path('export-to-excel-user-types/', views.export_to_excel_user_types, name='export-to-excel-user-types'),
    path('export-to-excel-user-domains/', views.export_to_excel_user_domains, name='export-to-excel-user-domains'),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)