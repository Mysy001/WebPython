from flask import Blueprint

#创建蓝图
Admin = Blueprint("admin",__name__)

@Admin.route('/')
def index():
    return ' <h1> Hello Admin <h1> '