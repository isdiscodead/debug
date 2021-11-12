from django.urls import path

from hunterapp import views
from hunterapp.views import *

app_name = "hunterapp"

urlpatterns = [
    path('create/', HunterCreateView.as_view(), name='create'),
    path('list/', HunterListView.as_view(), name='list'),
    path('detail/<int:pk>', HunterDetailView.as_view(), name='detail'),
    path('update/<int:pk>', HunterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.hunter_delete, name='delete'),
]
