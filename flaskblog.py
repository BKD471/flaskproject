from flask import Flask,flash,render_template,url_for,redirect
from forms import RegistrationForm,LoginForm
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='738fe18c28bdef0df978d24442c5eba37a8540f7510067238953c6e3841cd91ee13d9032903d8a17cf9d2adf16979bbde9c2b811bb331872fe80d96d3b67256f994b93954964889d33f0e8c9e00862d75f53d628ea07589fac05a4c7b22eecc1e8ba8712f0118ca48300a5cdc827c67fa7bad275700a91ad2274eb00d034ad0a6414aeeb85d533dd4cd3c9291b4eb1c59ea2b409d300e10212a1d299c15daa1f198c9d5541e8ce2e2d3582b91c8a7c910ed634513cb04f3377ab5b13df3f3f96d1078e7cfaf0a61981e71ff4d83d81ae52c4dec46a86c9e766a0fc5069a7aaca133851e643e39f895af3c09b2d7df184e6f973bb24ab186bb08f3ee7261998ce'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

#class represent model which is table in the database insides
class User(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(20),unique=True,nullable=False)
  email=db.Column(db.String(120),unique=True,nullable=False)
  image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
  password=db.Column(db.String(60),nullable=False)
  posts=db.relationship('Post',backref='author',lazy=True)


  def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(100),nullable=False)
  date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  content=db.Column(db.Text,nullable=False)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  

  def __repr__(self):
    return f"Post('{self.title}','{self.date_posted}')"


posts=[
    {'author':'Bhaskar',
      'title':'Blog post 1',
      'content':'first content',
      'date':'12th January,2020'
    },
    {'author':'John Doer',
      'title':'Blog post 2',
      'content':'second content',
      'date':'10th January,2020'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='about blogs')

@app.route("/register",methods=['GET','POST'])
def registration():
    form=RegistrationForm()
    if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!','success')
      return redirect(url_for('home'))

    return render_template("register.html",title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
      if form.email.data=='admin@blog.com' and form.password.data=='password':
        flash('You are logged in!','success')
        return redirect(url_for('home'))
      else:
        flash('Wrong username or password','danger')  
    return render_template("login.html",title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)