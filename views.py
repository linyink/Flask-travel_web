"""
这是视图函数
"""
"""
一点小心得：
redirect(url_for())是重定向到对应的视图函数名，由对应的视图函数来渲染模板。
render_template()是渲染模板，一般只写在对应的视图函数下面。
最重要的区别就是：
url_for()里面写的参数是传给视图函数中的，而render_template()里面的参数是传给视图函数的。
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import config
from models import User, Topic, Answer
from exts import db
from decorators import login_required
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

# 好的，现在已经跑通了数据库的登录和注册了
# 自己写的服务器就不要去贪图省力就用数据库迁移，就自己写吧
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        # # 用于测试，暂时还没有数据库
        # # 这样写是没有问题的，说明能够接收到我的post请求
        # if telephone == "1" and password == "1":
        #     return render_template('index.html')
        # else:
        #     flash(u"错了")

        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        # redirect()主要连接的是html,url_for()连接的是视图函数名
        else:
            flash('手机号码或者密码不正确')
            return redirect(url_for('login'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证，如果被注册了就不能用了
        # first()返回第一条数据
        user = User.query.filter(User.telephone == telephone).first()
        # 如果user有数据，即为真
        if user:
            flash(u'该手机号码被注册，请更换手机')
            return redirect(url_for('register'))
        else:
            # password1 要和password2相等才可以
            if password1 != password2:
                flash(u'两次密码不相等，请核实后再填写')
                return redirect(url_for('register'))
            else:
                user = User(telephone=telephone, username=username, password=password1)
                # 将数据提交到数据库中
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转到登录的页面(重定向)
                return redirect(url_for('login'))


# 旅游介绍
@app.route('/details/')
def details():
    return render_template('details.html')

# 加入我们
@app.route('/joinUs/')
def joinUs():
    return render_template('join_us.html')


# 是搜索出了问题，然后内容是搜索不到了
@app.route('/search/')
def search():
    q = request.args.get('q')
    topics = Topic.query.filter(Topic.title.contains(q), Topic.content.contains(q))
    return render_template('all_topic.html', topics=topics)
    # return redirect(url_for('topic_detail', topics=topics))


# publish_topic是发布页面，
@app.route('/publish_topic/', methods=['GET', 'POST'])
@login_required
def publish_topic():
    if request.method == 'GET':
        return render_template('publish_topic.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        topic = Topic(title=title, content=content)
        # 获得当前的用户id
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        topic.author = user
        db.session.add(topic)
        db.session.commit()
        # flash(u'发布成功') 页面跳转的太快了看不到
        return redirect(url_for('all_topic'))  # 这里原来是topic_detail

# 相当于话题详情页面
# 流程是all_topic-->topic_detail
@app.route('/topic_details/<topic_id>/')
def topic_details(topic_id):
    topic_model = Topic.query.filter(Topic.id == topic_id).first()
    return render_template('topic_details.html', topic=topic_model)
   #  return redirect(url_for('topic_detail', topic=topic_model))


# 怪不得模板一直报错说topic没有定义呢
@app.route('/all_topic/')
def all_topic():
    context = {
        'topics': Topic.query.order_by('create_time').all()
    }
    # **以自典的形式传
    return render_template('all_topic.html', **context)


@app.route('/add_answer/', methods=['GET', 'POST'])
@login_required  # 登陆限制装饰器
def add_answer():
    content = request.form.get('answer_content')
    topic_id = request.form.get('topic_id')
    # 一直评论不成功，是因为将评论要插入哪个表写错了，而且topic_id也要传入才行
    answer = Answer(content=content, topic_id=topic_id)  # 实例化类Answer
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    answer.author = user
    topic = Topic.query.filter(Topic.id == topic_id).first()
    answer.topic = topic
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('topic_details', topic_id=topic_id))


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


# 上下文处理器钩子函数,钩子函数(注销)
# 维持user_id的登录状态
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            # 必须返回自典类型
            return {'user': user}
    return {}


# @app.route('/topic_details/')
# def topic_details():
#     return render_template('topic_details.html')


if __name__ == '__main__':
    app.run(debug=True)