# _*_ encoding:utf-8 _*_
__author__ = 'xyx'
__date__ = '2017-6-4 '

import xadmin

from .models import EmailVerifyRecord, Banner
from xadmin import  views

class Basesetting(object):
    enable_themes = True
    use_bootswatch = True

class Globalsettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "XYX"
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, Basesetting)
xadmin.site.register(views.CommAdminView, Globalsettings)