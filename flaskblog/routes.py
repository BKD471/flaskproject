from flask import flash,render_template,url_for,redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm,LoginForm

from flaskblog.models import User,Post


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
      hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user=User(username=form.username.data,email=form.email.data,password=hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created:You are now able to  login','success')
      return redirect(url_for('login'))

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