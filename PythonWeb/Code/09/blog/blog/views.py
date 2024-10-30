from django.http import HttpResponse

def article_list(request):
    return HttpResponse('article_list函数')

def year_archive(request,year):
    return HttpResponse(f'year_archive函数接受参数year:{year}')

def month_archive(request,year,month):
    return HttpResponse(f'month_archive函数接受参数year:{year},month:{month}')

def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail函数接受参数year:{year},month:{month},slug:{slug}')

def article_re(request,year):
    return HttpResponse(f"正则表单式year is{year}")


