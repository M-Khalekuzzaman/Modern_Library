from django.urls import path
from .import views

urlpatterns = [
    path('registration/',views.registration, name = 'registration_page'),
    path('login/',views.logIn, name = 'login_page'),
    path('profile/',views.profile, name = 'profile_page'),
    path('change_password/',views.change_password, name = 'change_password'),
    path('logout/',views.logOut, name = 'logout_page'),
    path('dashboard/',views.dashboard, name = 'dashboard_page'),
    path('change_password_without_oldpass/',views.change_password_without_oldpass, name = 'changepass_without_oldpass'),
    path('edit_profile/',views.user_update_info, name = 'edit_profile'),
    
    
]
