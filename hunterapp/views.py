from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from hunterapp.decorators import request_ownership_required
from hunterapp.forms import HunterCreationForm
from hunterapp.models import Hunter


class HunterListView(ListView):
    model = Hunter
    context_object_name = 'hunter_list'
    template_name = 'hunterapp/list.html'
    paginate_by = 8


@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'post')
class HunterCreateView(CreateView):
    model = Hunter
    context_object_name = 'target_hunter'
    form_class = HunterCreationForm
    template_name = 'hunterapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('requestapp:detail', kwargs={'pk': self.object.pk})


class HunterDetailView(DetailView):
    model = Hunter
    context_object_name = 'target_hunter'
    template_name = 'hunterapp/detail.html'


@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('userapp:login')), 'post')
@method_decorator(request_ownership_required, 'get')
@method_decorator(request_ownership_required, 'post')
class HunterUpdateView(UpdateView):
    model = Hunter
    context_object_name = 'target_hunter'
    form_class = HunterCreationForm
    template_name = 'hunterapp/update.html'

    def get_success_url(self):
        return reverse('hunterapp:detail', kwargs={'pk': self.object.pk})


@login_required(login_url='/users/login/')
@request_ownership_required
def hunter_delete(request, pk):
    quest = Hunter.objects.get(pk=pk)
    if quest.writer == request.user:
        quest.delete()
        return HttpResponseRedirect(reverse('home'))