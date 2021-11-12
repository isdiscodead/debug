from django.urls import path

from requestapp import views
from requestapp.views import RequestUpdateView, RequestListView, RequestCreateView, RequestDetailView

app_name = "requestapp"

urlpatterns = [
    path('create/', RequestCreateView.as_view(), name='create'),
    path('list/', RequestListView.as_view(), name='list'),
    path('detail/<int:pk>', RequestDetailView.as_view(), name='detail'),
    path('update/<int:pk>', RequestUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.request_delete, name='delete'),
]
