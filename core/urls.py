from django.contrib.auth import logout
from django.urls import path
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path("login/", LoginView.as_view(), {"template_name": 'core/login.html' }, name="login"  ),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout")

]

