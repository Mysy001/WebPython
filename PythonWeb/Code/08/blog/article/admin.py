from django.contrib import admin
from article.models import User,Article

class UserAdmin(admin.ModelAdmin):
    """
    创建UserAdmin类，继承于admin.ModelAdmin
    """
    #  配置展示列表，在User版块下的列表展示
    list_display = ('username', 'email')
    # 配置过滤查询字段，在User版块下右侧过滤框
    list_filter = ('username', 'email')
    # 配置可以搜索的字段，在User版块下右侧搜索框
    search_fields = (['username','email'])

class ArticleAdmin(admin.ModelAdmin):
    """
    创建UserAdmin类，继承于admin.ModelAdmin
    """
    #  配置展示列表，在User版块下的列表展示
    list_display = ('title', 'content','publish_date')
    # 配置过滤查询字段，在User版块下右侧过滤框
    list_filter = ('title',)  # list_filter应该是列表或元组
    # 配置可以搜索的字段，在User版块下右侧搜索框
    search_fields = ('title',) # search_fields应该是列表或元组

# 绑定User模型到UserAdmin管理后台
admin.site.register(User, UserAdmin)
# 绑定User模型到UserAdmin管理后台
admin.site.register(Article, ArticleAdmin)


