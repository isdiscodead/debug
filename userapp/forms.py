from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms


# from userapp.models import user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class SignupForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력 불가',
    }))
    nickname = forms.CharField(label='닉네임')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

        def clean_nickname(self):
            nickname = self.cleaned_data.get('nickname')
            if Profile.objects.filter(nickname=nickname).exists():
                raise forms.ValidationError("이미 존재하는 닉네임 입니다.")
            return nickname

        def clean_email(self):
            email = self.cleand_data.get('email')
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("사용중인 이메일 입니다.")
            return email

        def save(self):
            user = super().save()
            Profile.objects.create(
                user = user,
                nickname= self.cleand_data['nickname']
            )
            return user


class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


