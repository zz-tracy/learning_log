# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from learning_logs.models import Topic  # 导入我们要注册的模型Topic
from learning_logs.models import Entry  # 导入要注册的模型Entry

# Register your models here.
admin.site.register(Topic)  # 让django通过管理网站管理我们的Topic模型
admin.site.register(Entry)  # 让django通过管理网站管理我们的Entry模型
