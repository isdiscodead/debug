from django.urls import path

from userapp.views import AccountCreateView

app_name = "userapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view, name='create'),
]