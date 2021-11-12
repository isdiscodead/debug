from django.http import HttpResponseForbidden
from requestapp.models import Quest


def request_ownership_required(func):
    def decorated(request, *args, **kwargs):
        quest = Quest.objects.get(pk=kwargs['pk'])
        if not quest.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
