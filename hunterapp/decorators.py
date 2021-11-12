from django.http import HttpResponseForbidden
from hunterapp.models import Hunter


def request_ownership_required(func):
    def decorated(request, *args, **kwargs):
        hunter = Hunter.objects.get(pk=kwargs['pk'])
        if not hunter.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
