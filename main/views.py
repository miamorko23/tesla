# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User, Group


# @login_required(login_url="/login")
# def home(request):
#     return render(request, 'main/home.html')


# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/home')
#     else:
#         form = RegisterForm()

#     return render(request, 'registration/sign_up.html', {"form": form})

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .models import UserWithKey  # Make sure to import the updated User model

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = UserWithKey.objects.create_user(  # Use UserWithKey instead of User
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})