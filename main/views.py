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

# @login_required(login_url="/login")
# def home(request):
#     return render(request, 'main/home.html')

# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = UserWithKey.objects.create_user(  # Use UserWithKey instead of User
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1'],
#                 email=form.cleaned_data['email']
#             )
#             login(request, user)
#             return redirect('/home')
#     else:
#         form = RegisterForm()

#     return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = UserWithKey.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.address = form.cleaned_data['address']
            user.phone_number = form.cleaned_data['phone_number']
            user.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



# {FOR AI}

# from your_django_app.models import UserWithKey, DrowsinessEvent

# def record_drowsiness_event(secret_key, status):
#     try:
#         user = UserWithKey.objects.get(secret_key=secret_key)
#     except UserWithKey.DoesNotExist:
#         print("Invalid secret key")
#         return

#     DrowsinessEvent.objects.create(user=user, status=status)