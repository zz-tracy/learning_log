# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # 通过unicode_literals来使用python3中默认的编码unicode

from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # def __str__(self):  # python3的方法
    #     """返回模型的字符串表示"""
    #     return self.text

    def __unicode__(self):  # python2的方法
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)  # 按创建顺序呈现条目，并在每个条目旁边放置时间戳

    class Meta:  # 存储用于管理模型的额外信息
        verbose_name_plural = 'entries'  # 该属性可以在Django需要时使用Entries来表示多个条目

    def __unicode__(self):  # 告诉Django呈现条目时应显示哪些信息
        """返回模型的字符串表示"""
        return self.text[:50] + '...'  # 只显示text的前50个字符，并天添加了省略号，表示非整个条目
