from django.db import models


class Quest(models.Model):
    title = models.CharField(max_length=50, null=False)
    # writer = models.ForeignKey
    created_at = models.DateField(auto_now_add=True, null=True)

    img = models.ImageField(upload_to='request/', null=True)
    content = models.TextField(null=True)
    location = models.CharField(max_length=200, null=False)

    start_price = models.IntegerField(default=0)
    end_price = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)



    def __str__(self):
        title