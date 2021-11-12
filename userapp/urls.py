from django.urls import path
from userapp.views import *

from userapp.views import UserCreateView

app_name = "userapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', login_check, name='login'),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup")
]