from flask import Blueprint

# 创建蓝图
admin = Blueprint("admin",__name__)

@admin.route('/')
def index():
   return  '<h1>Hello Admin!</h1>'


