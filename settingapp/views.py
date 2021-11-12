from django.shortcuts import render

# Create your views here.
def option(request):
    return render(request, 'settingapp/option.html')