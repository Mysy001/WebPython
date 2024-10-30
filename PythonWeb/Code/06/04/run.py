from flask import Flask,url_for,redirect,render_template


app = Flask(__name__)

@app.route('/')
def index():
    name = "明日学院"
    message = """
        明日学院，是吉林省明日科技有限公司倾力打造的在线实用技能学习平台，该平台于2016年正式
        上线，主要为学习者提供海量、优质的课程，课程结构严谨，用户可以根据自身的学习程度，自主安
        排学习进度。我们的宗旨是，为编程学习者提供一站式服务，培养用户的编程思维。
    """
    return render_template("index.html",name=name,message=message)

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户名的用户信息
    return render_template("user.html",username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 根据ID显示文章，ID是整型数据
    return f'ID是:{post_id}'

@app.route('/login')
def login():
    # 模拟登录流程
    flag = 'success'
    # 如果登录成功，跳转到首页
    if flag:
        return redirect(url_for('hello_world'))
    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug = True)

