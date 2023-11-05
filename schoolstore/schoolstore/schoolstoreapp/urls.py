from . import views
from django.urls import path

app_name = 'schoolstoreapp'
urlpatterns = [
    path('', views.index, name='index'),

]