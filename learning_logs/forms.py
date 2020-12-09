# -*- coding: UTF-8 -*-

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:  # 通过一个内嵌类 "class Meta" 给 model 定义元数据
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:  # 通过一个内嵌类 "class Meta" 给 model 定义元数据
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # widget小部件，是一个html表单元素。
