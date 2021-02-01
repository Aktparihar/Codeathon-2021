from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def Login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            return render(request, 'MainPageAfterLogin.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def Register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get('name'), request.POST.get('email'), request.POST.get('password'))
        user.is_active = False
        user.first_name = request.POST.get('name')
        user.save()
        return render(request, 'MainPageAfterLogin.html')
    else:
        return render(request, 'register.html')
