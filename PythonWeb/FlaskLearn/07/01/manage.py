from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate

app = Flask(__name__)

#基本配置
app.config['SQLALCHEMY_DATABASE_URI']=(
    'mysql+pymysql://root:123456@localhost:3306/flask_demo'
    )
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #自动提交数据库会话中的改动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=Flask #设置为 True，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号

db = SQLAlchemy(app) #实例化SQLAlchemy
migrate = Migrate(app,db)

#创建数据库表
class User(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    articles = db.relationship('Article') #外键
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),index=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return '<Article %r>' % self.username     
    
    
if __name__ == '__main__':
    with app.app_context():        
        db.create_all()