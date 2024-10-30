from django.contrib import admin
from article.models import User, Article

from django.utils.translation import ugettext_lazy as _
from datetime import date


class PublishYearFilter(admin.SimpleListFilter):
    # 提供一个可读的标题
    title = _('发布年份')

    # 用于URL查询的参数
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        """
        重写lookups方法，返回一个二维元组。每个元组的第一个元素是用于URL查询的真实值，
        这个值会被self.value()方法获取，并作为queryset方法的选择条件。
        第二个元素则是可读的显示在admin页面右边侧栏的过滤选项。
        """
        return (
            ('2020', _('2020年')),
            ('2019', _('2019年')),
        )

    def queryset(self, request, queryset):
        """
        重写queryset方法，根据self.value()方法获取的条件值的不同执行具体的查询操作。
        并返回相应的结果。
        """
        if self.value() == '2019':
            return queryset.filter(publish_date__gte=date(2019, 1, 1),
                                   publish_date__lte=date(2019, 12, 31))
        if self.value() == '2020':
            return queryset.filter(publish_date__gte=date(2020, 1, 1),
                                   publish_date__lte=date(2020, 12, 31))


class UserAdmin(admin.ModelAdmin):
    """
    创建UserAdmin类，继承于admin.ModelAdmin
    """
    #  配置展示列表，在User版块下的列表展示
    list_display = ('username', 'email')
    # 配置过滤查询字段，在User版块下右侧过滤框
    list_filter = ('username', 'email')
    # 配置可以搜索的字段，在User版块下右侧搜索框
    search_fields = (['username', 'email'])


class ArticleAdmin(admin.ModelAdmin):
    """
    创建ArticleAdmin类，继承于admin.ModelAdmin
    """
    #  配置展示列表，在User版块下的列表展示
    list_display = ('id', 'title', 'publish_date')
    list_display_links = ('id',)
    # list_editable = ('title', 'publish_date')
    # 配置过滤查询字段，在User版块下右侧过滤框
    list_filter = ('title', 'user__username', PublishYearFilter)  # list_filter应该是列表或元组
    # 配置可以搜索的字段，在User版块下右侧搜索框
    search_fields = ('title',)  # search_fields应该是列表或元组
    # 显示字段
    # fields = (('id','title'),'content','publish_date')

    fieldsets = (
        ('Main', {
            'fields': ('id', 'title', 'publish_date')
        }),
        ('Advance', {
            'classes': ('collapse',),
            'fields': ('content',),
        })
    )


# 绑定User模型到UserAdmin管理后台
admin.site.register(User, UserAdmin)
# 绑定User模型到UserAdmin管理后台
admin.site.register(Article, ArticleAdmin)
