from . import views
from django.urls import path
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('form', views.form, name="form"),
    path('index', views.index, name="index"),
    path('logout', views.logout, name="logout"),


]