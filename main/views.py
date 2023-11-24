from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserWithKey
from django.contrib.auth.decorators import login_required
from .models import DrowsinessEvent

@login_required(login_url="/login")
def user_events(request):
    user_events = DrowsinessEvent.objects.filter(user=request.user)
    return render(request, 'main/user_events.html', {'user_events': user_events})

@login_required(login_url="/login")
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.userwithkey.address = form.cleaned_data.get('address')
            request.user.userwithkey.phone_number = form.cleaned_data.get('phone_number')
            request.user.userwithkey.save()
            return redirect('/home')
    else:
        form = UpdateProfileForm(initial={'address': request.user.userwithkey.address, 'phone_number': request.user.userwithkey.phone_number}, instance=request.user)
    return render(request, 'main/update_profile.html', {'form': form})

def home(request):
    user_events = DrowsinessEvent.objects.filter(user=request.user)
    return render(request, 'main/home.html', {'user_events': user_events})

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
