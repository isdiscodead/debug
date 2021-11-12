from django.shortcuts import render

# Create your views here.
def userhome(request):
    return render(request, 'profileapp/userhome.html')