from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('update-profile', views.update_profile, name='update_profile'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='main/change_password.html', success_url='/'), name='change_password'),    
    path('approve-manager/<int:user_id>/', views.approve_manager, name='approve_manager'),
    path('manager-approval', views.manager_approval, name='manager_approval'),
    path('approved-managers', views.approved_managers, name='approved_managers'),
]