from flask import Flask #导入flask 类

#创建该类的一个实例(第一个参数是应用模块或包的名称，如果使用单一模块，名称为__name__)
app = Flask(__name__)

#使用 route() 修饰器告诉 Flask 什么样的 URL 能触发执行被修饰的函数
@app.route('/')

#返回显示在用户浏览器中的信息
def index():
    return 'Hello World!'

#使用run() 函数来让应用运行在本地服务器上
if __name__ == '__main__':
    app.run()