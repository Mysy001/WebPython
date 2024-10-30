from flask import Blueprint

#创建蓝图
home = Blueprint("home",__name__)

@home.route('/')
def index():
    return '<h1> Hello Home <h1>'