from django.conf.urls import url

from account import views

urlpatterns = [
    url('login/', views.login_view, name='login')
]
