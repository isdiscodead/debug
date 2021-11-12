from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=20, unique=True)

    GENDER_C = (
        ('선택안함', '선택안함'),
        ('남성','남성'),
        ('여성', '여성')
    )
    gender = models.CharField('성별(선택사항)', max_length=10, choices=GENDER_C, default='N')
    about = models.CharField(max_length=300, blank=True)
    #callnumber = models.CharField(max_length=13)

    # 추천수는 정수 필드
    #recommend = models.IntegerField(default=0)

    # 0 업체, 1 의뢰인, 2 헌터
    #usercategory = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])

    # 별점 5점까지 제한, 기본 0점
    #avereputation = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.nickname
