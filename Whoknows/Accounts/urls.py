from django.urls import path
from .views import SignUpView,LoginView


urlpatterns = [
    path('',LoginView.as_view(),name='login'),
    path('signup',SignUpView.as_view(),name='signup')
]
