from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from apps.organization.models import CourseOrg, Teacher, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organization.form import UserAskForm
import json

class OrgListView(View):
    
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        # 热门机构
        hot_orgs = all_orgs.order_by("-click_nums")[:5]

        # 城市筛选的逻辑
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        
        # 类别筛选的逻辑:
        cateory = request.GET.get('ct', "")
        if cateory:
            all_orgs = all_orgs.filter(org_type=str(cateory))

        # 排序的逻辑
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by("-course_nums")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        # 获取到所有的课程机构
        org_nums = all_orgs.count()
        # 获取所有的开通城市
        all_city = CityDict.objects.all()
        cav = 'org_list'
        return render(request, 'org-list.html', {
            'cav': cav,  # 用来判断当前是哪个页面
            'all_orgs': orgs,
            'all_citys': all_city,
            'org_nums': org_nums,
            "city_id": city_id,
            'cateory': cateory,
            'hot_orgs': hot_orgs,
            "sort": sort,
        })


class AddAskView(View):
    """
    用户咨询表单提交
    技术点:
    Modelform表单的具体应用
    ajx的异步操作, 仅操作部分内容,而不刷新整个页面.
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # 在这里直接调用Modelform进行数据保存
            user_ask = userask_form.save(commit=True)
            content = {
                'status': 'success',
            }
            return HttpResponse(json.dumps(content), content_type='application/json')
        else:
            content = {
                'status': 'fail',
                'msg': "添加错误",
            }
            return HttpResponse(json.dumps(content), content_type='application/json')



class OrgHomeView(View):
    """
    用户机构首页
    
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 外键的应用 实例
        all_courses = course_org.courses_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'all_teachers': all_teachers,
        })
