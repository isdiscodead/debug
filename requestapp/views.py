from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


def home(request):
    return render(request, 'requestapp/list.html')

# class ArticleListView(ListView):
#     model = Article
#     context_object_name = 'article_List'
#     template_name = 'articleapp/list.html'
#     paginate_by = 8
