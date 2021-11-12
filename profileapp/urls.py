from django.urls import path

from profileapp.views import userhome

app_name = "profileapp"

urlpatterns = [
    path('', userhome, name='userhome'),

]