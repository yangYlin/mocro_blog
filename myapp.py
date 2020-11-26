from flask import Flask, request, abort, render_template
from flask_bootstrap import Bootstrap

from MyForm import MyForm
from dao.People  import User,Role,db

from  flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world'

bootstrap = Bootstrap(app) #Twiter的前端框架
migrate = Migrate(app.db) #数据库迁移

#装饰器
@app.route('/')
def hello_world():
    ueserAgent = request.headers.get('user-agent')
    print(ueserAgent)

    # 类
    class Person(object):
        name = u'p17bdw'
        age = 18

    p = Person()

    context = {
        'username': u'c17bdw',
        'gender': u'男',
        'age': 17,
        'person': p,  # 声明
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    books = [
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 109
        },
        {
            'name': u'红楼梦',
            'author': u'曹雪芹',
            'price': 200
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 120
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price': 130
        }
    ]
    #return render_template('index.html',**context,Books=books)
    return render_template('index.html',Books=books)


@app.route('/user/<name>')
def user(name):
    #abort(404)
    return render_template('user.html', name=name)


@app.route('/comments')
def comments():
    comments = [
        {
            'user': u'admin',
            'content': 'xxxx'
        },
        {
            'user': u'tesr',
            'content': 'xxxx'
        }
    ]

    return render_template('comments.html',comments=comments)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login/',methods= ['GET','POST'])
def login():
    name = None
    form = MyForm()
    if form.validate_on_submit():
        name =form.name.data
        form.name.data = ''
    return render_template('login.html',form = form, name =name)

@app.shell_context_processor
def make_shell_context():
    return  dict(db=db,User = User,Role = Role)
if __name__ == '__main__':
    app.run(debug=True)
