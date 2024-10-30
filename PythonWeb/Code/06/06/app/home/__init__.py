from flask import Blueprint

home = Blueprint("home",__name__)

# 创建蓝图
@home.route('/')
def index():
   return  '<h1>Hello Home!</h1>'


