from django.urls import path

from requestapp.views import RequestUpdateView, RequestDeleteView, RequestListView, RequestCreateView
from settingapp.views import option

app_name = "settingapp"

urlpatterns = [
    path('', option, name='option'),

]
