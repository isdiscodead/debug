from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from pytz import timezone
from Debug import settings


class Hunter(models.Model):
    title = models.CharField(max_length=50, null=False)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='hunter', null=True)
    created_at = models.DateTimeField(default=now, editable=False)

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)
    content = models.TextField(null=True)
    location = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.title
