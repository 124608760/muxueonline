# _*_ encoding:utf-8 _*_
__author__ = 'xyx'
__date__ = '2017-7-13 21:56'

from django import forms

from operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']