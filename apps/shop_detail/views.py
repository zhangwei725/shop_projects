from django.shortcuts import render

from apps.home.models import Shop
# 异步 邮件功能

def detail(request):
    if request.method == 'GET':
        try:
            ship_id = request.GET.get('id')
            if ship_id:
                shop = Shop.objects.get(shop_id=ship_id)
                shop.imgs = shop.shopimage_set.all()
                return render(request, 'detail.html', {'shop': shop})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
