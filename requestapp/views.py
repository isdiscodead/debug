from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from requestapp.models import Quest


def home(request):
    return render(request, 'requestapp/list.html')


class ArticleListView(ListView):
    model = Quest
    context_object_name = 'request_List'
    template_name = 'requestapp/list.html'
    paginate_by = 8
