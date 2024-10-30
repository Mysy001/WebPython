from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.shortcuts import render,redirect
from article.models import Article,User
from article.forms import LoginForm

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
            email = form.cleaned_data['email']
            # 页面跳转至欢迎页
            # return HttpResponseRedirect('/articles/welcome',username=username)
            return HttpResponse(f'用户名:{username} ，邮箱:{email}')
        else:
            return render(request, 'login.html', {'form': form})

