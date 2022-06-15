from django.urls import path
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as user_creations
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, UserSetPasswordForm, CustomUserCreationForm
from . import views

urlpatterns = [
    path('log_in/', views.user_login, name='log_in'),

    path('log_in/', auth_view.LoginView.as_view(), name='log_in'),

    path('logout/', auth_view.LogoutView.as_view(next_page='home'), name='logout'),

    path('password_reset/', auth_view.PasswordResetView.as_view(
        template_name="registration/reset_password.html", form_class=UserPasswordResetForm),
         name="password_reset"),
    path('password_reset_sent/', auth_view.PasswordResetDoneView.as_view(
        template_name="registration/reset_password_sent.html"),
         name="password_reset_done"),
    path('password/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name="registration/reset_password_set.html", form_class=UserSetPasswordForm),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name="registration/reset_password_complete.html",
    ), name="password_reset_complete"),

    path('sing-up/', views.user_registration, name='sing-up'),

]