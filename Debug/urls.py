from django.contrib import admin
from django.urls import path, include

from requestapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RequestListView.as_view(), name='home'),
    path('users/', include('userapp.urls')),
    path('requests/', include('requestapp.urls')),
]
