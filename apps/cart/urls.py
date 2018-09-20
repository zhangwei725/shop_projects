from django.conf.urls import url

from apps.cart import views

urlpatterns = [
    url('add/', views.add),
    url('list/', views.list, name='car_list')
]
