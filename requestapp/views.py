from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from requestapp.decorators import request_ownership_required
from requestapp.forms import QuestCreationForm
from requestapp.models import Quest


class RequestListView(ListView):
    model = Quest
    context_object_name = 'request_list'
    template_name = 'requestapp/list.html'
    paginate_by = 8


@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'post')
class RequestCreateView(CreateView):
    model = Quest
    context_object_name = 'target_request'
    form_class = QuestCreationForm
    template_name = 'requestapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('requestapp:detail', kwargs={'pk': self.object.pk})


class RequestDetailView(DetailView):
    model = Quest
    context_object_name = 'target_request'
    template_name = 'requestapp/detail.html'


@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'post')
@method_decorator(request_ownership_required, 'get')
@method_decorator(request_ownership_required, 'post')
class RequestUpdateView(UpdateView):
    model = Quest
    context_object_name = 'target_request'
    form_class = QuestCreationForm
    template_name = 'requestapp/update.html'

    def get_success_url(self):
        return reverse('requestapp:detail', kwargs={'pk': self.object.pk})


@login_required(login_url='/users/login/')
# @request_ownership_required()
def request_delete(request, pk):
    quest = Quest.objects.get(pk=pk)
    if quest.writer == request.user:
        quest.delete()
        return HttpResponseRedirect(reverse('home'))