from django.contrib import admin
from django.urls import path
from home.views import dashboard
from apis import views

# admin creds for django panel
# admin@admin.com
# admin

urlpatterns = [
    # web views urls
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),

    # api urls
    path('api/users', views.UsersApiView.as_view()),
    path('api/bids', views.BidsApiView.as_view()),
    path('api/bids/<int:id>/', views.BidsApiView.as_view()),
    path('api/users-by-type/', views.UsersByTypeApiView.as_view()),
    path('api/refers', views.RefersApiView.as_view()),

]
