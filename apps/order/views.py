import datetime
import random
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render

from apps.home.models import ShopCar, Order, Shop
from django.db import transaction

"""
拿到所有被选中的购物车记录显示
# 



# 第一个 选择地址  
# 第二个  选择支付方式
# 第三个 配送方式
# 提交订单  操作订单表
# 1>生成订单号
# 2> 把商品的库存量减
# 3> 购物车表
# 多个表的查询  使用关联查询

# 增删改 涉及多个表   ---> 事务 原子性   一致性  隔离性(隔离级别) 持久性
"""


def confirm(request):
    # 被选中的商品信息
    ids = [12, 13, 14]
    cars = ShopCar.objects.filter(car_id__in=ids)
    return render(request, 'confirm.html', {'cars': cars})


# 字段 限定符
# 表与表之间有关联关系

#  结算---确认订单--生成订单 主表是订单表(order)
# @transaction.atomic()使用装饰器
def create_order(request):
    # 对多个表的操作  需要用到事务
    ids = [12, 13, 14]
    #     对订单表操作   --- 修改商品的库存 --- 修改购车表  将购物车记录状态设置订单的id
    # 第一步 生成订单号(要求必须是站内唯一)
    #     年月日时分秒
    # 表示开启事务
    order_code = f'{datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")}{random.randint(10, 99)}'
    try:
        # 推荐使用
        with transaction.atomic():
            #   第二歩 往订单表增加记录
            order = Order(order_code=order_code, address='湖北省武汉市', mobile=110, receiver='娇娇', user_message='请帮我带个男友',
                          user=request.user.userprofile)
            order.save()
            # 2表示用户已经购买了商品信息
            cars = ShopCar.objects.filter(car_id__in=ids)
            # 总金额
            total = 0.00
            for car in cars:
                car.status = 2
                car.order_id = order.pk
                car.save(update_fields=['status', 'order_id'])
                # 商品的库存
                if car.shop.stock >= car.number:
                    car.shop.stock -= car.number
                    car.shop.save(update_fields=['stock'])
                    total += car.number * float(str(car.shop.promote_price.quantize(Decimal('0.00'))))
                else:
                    # 生成订单
                    pass
            # 发起支付

    #         

    except Exception as e:
        return HttpResponse('2222')
    return HttpResponse('11111')
