from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import UserLogoutView, UserLoginView, RegisterView, verification, get_users_list

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('verify_message/', TemplateView.as_view(template_name='users/verify_message.html'), name='verify_message'),
    path('email/verify/<str:verify_code>', verification, name='verify'),
    path('success_verify/', TemplateView.as_view(template_name='users/success_verify.html'), name='success_verify'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path('users_list/', get_users_list, name='users')
]
