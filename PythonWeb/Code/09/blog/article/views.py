from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.shortcuts import render,redirect
from article.models import Article,User,ArticleModelForm,UserModelForm
from article.forms import LoginForm
from django.contrib.auth import authenticate, login , logout as django_logout
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def article_list(request):
    articles = Article.objects.all() # 从Article表中获取数据
    return render(request,'article_list.html',{"articles": articles}) # 渲染模板

def year_archive(request,year):
    return HttpResponse(f'year_archive函数接受参数year:{year}')

def month_archive(request,year,month):
    return HttpResponse(f'month_archive函数接受参数year:{year},month:{month}')

def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail函数接受参数year:{year},month:{month},slug:{slug}')

def article_re(request,year):
    return HttpResponse(f"正则表单式year is{year}")

def get_current_datetime(request):  # 定义一个视图方法，必须带有请求对象作为参数
    today = datetime.today()    # 请求的时间
    formatted_today = today.strftime('%Y-%m-%d')
    html = f"<html><body>今天是{formatted_today}</body></html>" # 生成html代码
    return HttpResponse(html)   # 将响应对象返回，数据为生成的html代码


class ArticleForm(View):
    def get(self, request, *args, **kwargs):  # 定义GET请求的方法
        return HttpResponse("返回get请求响应")

    def post(self, request, *args, **kwargs):  # 定义POST请求的方法
        return HttpResponse("返回post请求响应")

class LoginFormView(View):
    def get(self,request,*args,**kwargs):
        """
        定义GET请求的方法GET请求
        """
        return render(request,'login.html',{'form':LoginForm()})

    def post(self,request,*args,**kwargs):
        """
        定义POST请求的方法GET请求
        """
        # 将请求数据填充到LoginForm实例中
        form = LoginForm(request.POST)
        # 判断是否为有效表单
        if form.is_valid():
            # 使用form.cleaned_data获取请求的数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # 授权校验
            if user is not None:  # 校验成功，获得返回用户信息
                login(request, user)  # 登录用户，设置登录session
                return HttpResponseRedirect('/articles/')
            else:
                messages.add_message(request, messages.WARNING, '用户名和密码不匹配') # 提示错误信息

        return render(request, 'login.html', {'form': form})  # 渲染模板

def logout(request):
    """
    退出登录
    """
    django_logout(request)	# 清除response的cookie和django_session中记录
    return HttpResponseRedirect('/articles/login')

@login_required
def add_article(request):
    if request.method == 'GET':
        form = ArticleModelForm()  # 实例化表单类
    else:
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            return HttpResponse(f'验证成功')
    return render(request, 'add_article.html', {'form': form})  # 渲染模板
