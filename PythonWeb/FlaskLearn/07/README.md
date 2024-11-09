安装 Flask-SQLAlchemy 
    pip install Flask-SQLAlchemy
安装 Flask-Migrate
    pip install FLask-Migrate
安装 Flask-Script
    pip install flask-script

flask-migrate 扩展
    使用 FLASK_APP 环境变量定义如何载入应用
      set FLASK_APP=manage.py
    准备就绪，开始创建一个迁移环境
      flask db init
    创建完迁移环境后，自动生成迁移脚本
      flask db migrate -m "add gender for user table"
    更新数据库
      flask db upgrade
flask-script 扩展
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

出现问题
    https://www.ifrontend.net/2024/05/flask-script/