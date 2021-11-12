from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from requestapp.decorators import request_ownership_required
from requestapp.forms import QuestCreationForm
from requestapp.models import Quest


def home(request):
    return render(request, 'requestapp/list.html')


class RequestListView(ListView):
    model = Quest
    context_object_name = 'request_List'
    template_name = 'requestapp/list.html'
    paginate_by = 8


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class RequestCreateView(CreateView):
    model = Quest
    context_object_name = 'target_article'
    form_class = QuestCreationForm
    template_name = 'requestapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Quest
    context_object_name = 'target_request'
    template_name = 'requestapp/detail.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(request_ownership_required, 'get')
@method_decorator(request_ownership_required, 'post')
class RequestUpdateView(UpdateView):
    model = Quest
    context_object_name = 'target_request'
    form_class = QuestCreationForm
    template_name = 'requestapp/update.html'

    def get_success_url(self):
        return reverse('requestapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(request_ownership_required, 'get')
@method_decorator(request_ownership_required, 'post')
class RequestDeleteView(DeleteView):
    model = Quest
    context_object_name = "target_request"
    template_name = 'requestapp/delete.html'

    def get_success_url(self):
        return reverse('requestapp:list')