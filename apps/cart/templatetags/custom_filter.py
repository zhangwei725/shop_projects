"""
1> 语法格式
2> 内置过滤器
3>自定义过滤器
1>在app下新建一个templatetags的文件夹
2>在该文件下新建一个py文件
3> 实例化注册器  register = template.Library()
4> 声明过滤器(过滤器的本质是一个函数)
5> 注册过滤器 @register.filter
6> 可以在模板中使用
6.1> 在需要自定义的过滤器的模板中  {% load custom_filter %}
6.2>
"""
from django import template

# 实例化注册器 (规定格式)
register = template.Library()


# value|multiply:parmas
@register.filter
def multiply(value, p1):
    return value * p1


@register.filter
def multiply1(value, p1, p2):
    return value + p1 * p2


@register.simple_tag
def test_simple_tags(p1, p2, p3, p4):
    return p1 + p2 + p3 + p4
# 在模板中使用 { % test_simple_tags 1 2 3 4 %}
