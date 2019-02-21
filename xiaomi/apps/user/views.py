from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from  django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from mixin.mixin import LoginRequiredMixin
import re
from apps.user.models import *
# Create your views here.
class register(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        # 进行注册处理
        # 接收数据
        username = request.POST.get("username")
        passsword = request.POST.get("password")
        passsword_ensure = request.POST.get("ensure_pwd")
        phone=request.POST.get("phone")
        # 进行数据校验
        if not all([username, passsword,passsword_ensure, phone]):
            # 数据不完整
            return JsonResponse({"res":"error","msg":"请填写完整信息"})
        if passsword_ensure != passsword:
            return JsonResponse({"res":"error", "msg": "两次密码不一致"})
        if not re.match(r"1[3|4|5|7|8]\d{9}$", phone):
            return JsonResponse({"res":"error", "msg": "手机号格式错误"})
        # 检验用户名石是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return JsonResponse({"res":"error", "msg": "用户名重复"})
        # 进行业务处理，进行用户注册
        user = User.objects.create_user(username,"",passsword)
        user.phone = phone
        user.save()
        return JsonResponse({"res":"success", "msg": "注册成功"})

class login_view(View):
    def get(self, request):
        """  显示登录页面"""
        # 判断是否记住了用户名 如果username在后台cookie里，得到cookie里的username
        if "username" in request.COOKIES:
            username = request.COOKIES.get("username")
            # checked默认被选中
            checked = "checked"
        else:
            username = ""
            checked = ""
        return render(request, "login.html", {"username": username, "checked": checked})

    def post(self, request):
        """  登录校验"""
        # 1、接收数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        print(username,password)
        # 2、校验数据
        if not all([username, password]):
            return render(request,"login.html",{"errmsg":"请填写完整信息"})
        # 业务处理 登录校验
        user = authenticate(username=username, password=password) #注意authenticate指令只能验证用户名和密码
        if user is not None:
            # # 用户名密码正确
             # 记录用户的登录状态
            login(request, user)
            response = request.GET.get("next",redirect("goods:index"))
            # 判断是否需要记住用户名
            if remember == "on":
                # 点击了，记住了用户名，设置cookie过期时间7天，需3个参数
                response.set_cookie("username", username, max_age=7 * 24 * 3600)

            else:
                response.delete_cookie("username")  # 删除cookie
            # 返回首页
            return response
        else:
            # 用户名或密码错误
            return render(request, "login.html", {"errmsg": "用户名或密码错误"})

