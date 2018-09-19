from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#  在父类容器使用 相对定位
#  在子元素中使用  绝对定位   left  top  bottom right   z-index
#
from apps.home.models import ShopCar


def login_view(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user and user.is_active:
        user.userprofile.count = ShopCar.objects.filter(user_id=user.userprofile.uid).aggregate(Sum('number'))
        login(request, user)
    return HttpResponse(11111)
