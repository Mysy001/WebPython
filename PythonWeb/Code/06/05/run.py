from flask import Flask ,url_for,redirect, render_template
from models import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mrsoft'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录页面
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        if username== "andy" and password == "mrsoft":
            return redirect(url_for('index'))
    return render_template('upload.html',form=form)

@app.route('/')
def index():
    """
    首页
    """
    name = "明日学院"
    message = """
        明日学院，是吉林省明日科技有限公司倾力打造的在线实用技能学习平台，该平台于2016年正式
        上线，主要为学习者提供海量、优质的课程，课程结构严谨，用户可以根据自身的学习程度，自主安
        排学习进度。我们的宗旨是，为编程学习者提供一站式服务，培养用户的编程思维。
    """
    return render_template("index.html",name=name,message=message)

if __name__ == '__main__':
    app.run(debug=True)
