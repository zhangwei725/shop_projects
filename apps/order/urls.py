from django.conf.urls import url

from order import views

urlpatterns = [
    url('create/', views.create_order, name='order_create')
]
