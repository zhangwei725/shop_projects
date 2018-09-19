from django.db.models import F
from django.http import HttpResponse

from apps.home.models import ShopCar
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add(request):
    # if request.is_ajax()
    try:
        """
        参数  商品的数量
        参数   商品的id
        """
        uid = 1
        shop_id = request.POST.get('shop_id')
        number = request.POST.get('number')
        """
        当商品已经存在用户的购物车的时候,更新数量
        当商品不存在用户的购物车的时候 创建该记录
        """
        cars = ShopCar.objects.filter(user_id=uid, shop_id=shop_id, status=1)
        if cars:
            car = cars.first()
            #     表示存在就去更新
            car.number = F('number') + number
            # car.number += number
            car.save(update_fields=['number'])
        else:
            car = ShopCar(user_id=uid, shop_id=shop_id, number=number)
            car.save()
        return HttpResponse('1111')
    except Exception as  e:
        pass
    return HttpResponse('1111')


def delete(request):
    pass


def update_num(request):
    pass


def find(request):
    pass
