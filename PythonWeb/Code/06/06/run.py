from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(home_blueprint, url_prefix='/home')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
