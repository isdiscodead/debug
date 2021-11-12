from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

# from userapp.models import user

class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True #초기화 이후에 유저네임을 비활성화 : 유저 네임은 고유하게  바꿀 수 없도록

# class AccountCreationFrom(ModelForm):
#     class Meta:
#         model = user
#
#         name = models.cg