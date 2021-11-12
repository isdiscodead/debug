from django.contrib import admin
from django.urls import path, include
from requestapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', include('userapp.urls')),
    path('requests/', include('requestapp.urls')),
    path('settings/',include('settingapp.urls')),
]
