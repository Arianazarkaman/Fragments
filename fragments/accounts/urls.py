from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name="registeration"),
    path('login/', views.UserLoginAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
]