from django.urls import path    # 导入path
from . import views             # 导入自定义的views模块

urlpatterns = [
    path('', views.article_list),
    path('<int:year>/', views.year_archive),
    path('<int:year>/<int:month>/', views.month_archive),
    path('<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('current',views.get_current_datetime),
    path('login',views.LoginFormView.as_view())
]
