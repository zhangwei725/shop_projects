from django.conf.urls import url

from shop_detail import views

urlpatterns = [
    url('detail/', views.detail, name='detail')
]
