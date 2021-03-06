from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from requestapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RequestListView.as_view(), name='home'),
    path('users/', include('userapp.urls')),
    path('requests/', include('requestapp.urls')),
    path('settings/',include('settingapp.urls')),
    path('profile/', include('profileapp.urls')),
    path('hunters/', include('hunterapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

