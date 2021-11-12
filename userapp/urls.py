from django.urls import path

from userapp.views import UserCreateView

app_name = "userapp"

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
]