# -*- coding: UTF-8 -*-
"""定义learning_logs的URL模式"""

from django.conf.urls import url  # 导入函数url, 使用它来将URL映射到视图

from . import views  # 句点让python从当前的urls.py模块所在的文件中导入视图

urlpatterns = [
    # 主页
    url(r'^$',  # 第一个参数：正则表达式，django在urlpatterns中查找与请求的URL字符串匹配的正则表达式
        views.index,   # 第二参数：指定了要调用的视图函数，当请求的URL与前述正则表达式匹配时，调用views.index
        name='index'  # 第三个参数：将这个URL模式的名称指定为index,让我们能够在代码其他地方引用它。
        ),
]
