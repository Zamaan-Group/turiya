from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('verify-register/', views.VerifyPhoneRegisterAPIView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('change-password/', views.ChangePasswordView.as_view()),
    path('reset-password/', views.ResetPasswordView.as_view()),
    path('check-reset-password', views.CheckResetPasswordAPIView.as_view()),
    path('confirm-set-password/', views.ConfirmResetPasswordView.as_view()),
    path('rud-myaccount/<int:pk>/', views.MyAccountRUDAPIView.as_view()),
]
