from django.urls import path
from. import views
app_name='icecreamapp'
urlpatterns = [
  path('',views.index,name="index"),
  path('icecream/<int:icecream_id>/',views.detail,name="detail"),
  path('add/',views.add_icecream,name='add_icecream'),
  path('update/<int:id>/',views.update,name="update"),
  path('delete/<int:id>/',views.delete,name="delete")
]