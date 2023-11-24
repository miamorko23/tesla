from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='main/change_password.html', success_url='/'), name='change_password'),
]

# path('user_events', views.user_events, name='user_events'),