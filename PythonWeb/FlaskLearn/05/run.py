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
        if username== "bai" and password == "123456":
            return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/')
def index():
    name = "重庆工程学院"
    message = """
        重庆工程学院（Chongqing Institute of
        Engineering）位于重庆市，是经教育部批准设立的一所以工学为主的全日制普通本科高校，是中央财政支持建设院校、全国物联网技术应用人才培养基地、全国动漫游戏产业人才培养基地、重庆市软件产业人才培养基地、重庆市创意产业人才培养基地，入选重庆市首批示范性众创空间。
        学校成立的“金融大数据智能应用重庆市高校工程研究中心 [17]”为重庆市智能领域科技创新平台，“重庆市数字影视与新媒体工程技术研究中心 [18]”为市级工程技术研究中心，“中华文化动漫研发传播中心
        [19]”为市级科普基地，“虚拟现实（VR）应用技术研究中心 [20]”为市级高校创新团队，“智能制造物联网应用技术研究中心
        [21]”为市级高校创新团队。其软件工程学科为重庆市重点培育学科，物联网工程专业为重庆市本科高校一流专业
        [23]、“软件工程”和“物联网工程"专业为重庆市特色本科专业。近年来，学校组织学生参加全国及省市级学科竞赛中荣获800余项奖励，在同类院校中位居前列。 [22]
        据2024年5月学校官网显示，学院设有南泉和双桥两个校区，设有8个二级学院，开设28 [25]个本科专业（类）；在校学生16000余人。 [1]
            """
    return render_template('index.html',name=name,message=message)

if __name__ == '__main__':
    app.run(debug=True)