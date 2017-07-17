# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
# Create your views here.

class OrgView(View):                                           # 课程机构列表功能
    def get(self, request):
        all_orgs = CourseOrg.objects.all()          # 机构
        hot_orgs = all_orgs.order_by("-click_num")[:3]
        all_citys = CityDict.objects.all()          # 城市

        city_id = request.GET.get('city','')       # 取出筛选城市
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct','')       # 取出筛选类别
        if category:
            all_orgs = all_orgs.filter(category=category)

        org_nums = all_orgs.count()

        sort = request.GET.get('sort','')       # 取出排序
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count()


        try:                                       # 分页
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        objects = ['john', '']
        context = {}
        context["all_orgs"] = orgs
        context["category"] = category
        context["city_id"] = city_id
        context["all_citys"] = all_citys
        context["org_nums"] = org_nums
        context["hot_orgs"] = hot_orgs
        context["sort"] = sort
        return  render(request, "org-list.html", context)

class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type='json')
        else:
            return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors))