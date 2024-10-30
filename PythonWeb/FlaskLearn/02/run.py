from flask import Flask,url_for,redirect


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户名的用户信息
    return f'用户名是:{username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 根据ID显示文章，ID是整型数据
    return f'ID是:{post_id}'

if __name__ == '__main__':
    app.run(debug = True)


