from flask import Blueprint

#创建蓝图
Home = Blueprint("home",__name__)

@Home.route('/')
def index():
    return '<h1> Hello Home <h1>'