from alipay import AliPay
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from shop_projects import settings


def pay(request):
    # 创建支付宝对象
    alipay = AliPay(
        appid=settings.APP_ID,
        # 支付宝后台应用已经设置 可以使用默认的
        app_notify_url='http://127.0.0.1:9000/pay/callback/',
        app_private_key_string=settings.APP_PRIVATE_STRING,
        alipay_public_key_string=settings.APP_PUBLIC_STRING,
        sign_type="RSA",
        debug=True
    )
    # 生成订单数据
    # 电脑网站支付的地址 https://openapi.alipaydev.com/gateway.do?order_url
    order_url = alipay.api_alipay_trade_page_pay(
        subject='测试支付123456',
        out_trade_no='6666',
        total_amount='1.00',
        # 支付成功之后 前端跳转的界面 get请求
        return_url='https://www.baidu.com',
        # 后台接受支付宝支付相关的信息的接口  post请求
        # notify_url=
    )
    pay_url = settings.ALI_PAY_DEV_URL + order_url
    return redirect(pay_url)


# 支付成功跳转的url
@csrf_exempt
def notify_callback(request):
    json_data = request.POST.get('sign')

    pass
