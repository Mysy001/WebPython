from django.db import models       # 引入django.db.models模块
from django.forms import ModelForm,TextInput,DateInput,Textarea
from django import forms

class User(models.Model):
    """
    User模型类，数据模型应该继承于models.Model或其子类
    """
    id = models.IntegerField(primary_key=True)  # 主键
    username = models.CharField(max_length=30)  # 用户名，字符串类型
    email = models.CharField(max_length=30)     # 邮箱，字符串类型

    def __repr__(self):
        return User.username


class Article(models.Model):
    """
    Article模型类，数据模型应该继承于models.Model或其子类
    """
    id = models.IntegerField(primary_key=True)  # 主键
    title = models.CharField(max_length=20,verbose_name='标题')    # 标题，字符串类型
    content = models.TextField(verbose_name='内容')                # 内容，文本类型
    publish_date = models.DateTimeField(verbose_name='发布日期')       # 出版时间，日期时间类型
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 设置外键

    def __repr__(self):
        return Article.title

    def short_content(self):
        return self.content[:50]
    short_content.short_description = 'content'

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class ArticleModelForm(ModelForm):
    content = forms.CharField(
        label ='内容',
        widget=forms.Textarea(attrs={'class': "form-control"}),
        min_length=10,
        error_messages={
            'required': '内容不能为空',
            'min_length': '长度不能少于10个字符',
        }
    )
    class Meta:
        model = Article
        fields = ['title', 'content','publish_date']
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'publish_date': DateInput(attrs={'class': "form-control",'placeholder': "YYYY-MM-DD"}),
        }
        error_messages = {
            'title': {
                'required': "标题不能为空",
                'max_length': '长度不能超过20个字符',
            },
            'publish_date': {
                'required': "日期时间不能为空",
                'invalid': '请输入正确的日期格式'
            }
        }


