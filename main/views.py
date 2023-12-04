from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserWithKey
from django.contrib.auth.decorators import login_required
from .models import DrowsinessEvent
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator


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
        if request.user.is_superuser:
            return redirect('/home')
        form = UpdateProfileForm(initial={'address': request.user.userwithkey.address, 'phone_number': request.user.userwithkey.phone_number}, instance=request.user)
        form.fields.pop('password', None)
        form.fields.pop('password1', None)
        form.fields.pop('password2', None)
    return render(request, 'main/update_profile.html', {'form': form})


@login_required(login_url="/login")
def home(request):    
    if request.user.is_superuser or UserWithKey.objects.filter(pk=request.user.pk, is_manager=True, is_manager_approved=True).exists():
        all_user_events = DrowsinessEvent.objects.all().order_by('-time')
        # Filter by driver if specified
        driver_id = request.GET.get('driver')
        if driver_id:
            all_user_events = all_user_events.filter(user__id=driver_id)
        # Paginate the events
        paginator = Paginator(all_user_events, 10)  # Show 10 events per page
        page_number = request.GET.get('page')
        events = paginator.get_page(page_number)
        # Get all drivers
        all_drivers = UserWithKey.objects.filter(is_manager=False)
        if request.user.is_superuser:
            return render(request, 'main/superuser_dashboard.html', {'events': events, 'all_drivers': all_drivers})
        return render(request, 'main/all_user_events.html', {'events': events, 'all_drivers': all_drivers})
    else:
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
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            if form.cleaned_data['request_manager']:
                user.is_manager = True
                user.is_manager_approved = False
                user.is_active = False
                user.save()
            user.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})


@user_passes_test(lambda u: u.is_superuser)
def manager_approval(request):
    pending_requests = UserWithKey.objects.filter(is_manager=True, is_manager_approved=False)
    return render(request, 'main/manager_approval.html', {'pending_requests': pending_requests})


def approve_manager(request, user_id):
    request.user = UserWithKey.objects.get(pk=user_id)
    request.user.is_manager_approved = True
    request.user.is_active = True
    request.user.save()
    return redirect('manager_approval')


@user_passes_test(lambda u: u.is_superuser)
def approved_managers(request):
    approved_managers = UserWithKey.objects.filter(is_manager=True, is_manager_approved=True)
    return render(request, 'main/approved_managers.html', {'approved_managers': approved_managers})