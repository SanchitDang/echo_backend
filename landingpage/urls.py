import os
from django.urls import path
from .import views
from home.views import panel_login
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'echo_web_app')

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)

urlpatterns = [
    path('', views.landingpage, name='landingpage'),

    path('custom-login/', views.custom_login, name='custom_login'),
    path('login-admin/', panel_login, name='login_admin'),

    path('login-user/', lambda r: flutter_redirect(r, 'index.html'), name='login_user'),
    path('login-user/<path:resource>', flutter_redirect),

  
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)