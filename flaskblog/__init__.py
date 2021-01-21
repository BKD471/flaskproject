from flask import Flask
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='738fe18c28bdef0df978d24442c5eba37a8540f7510067238953c6e3841cd91ee13d9032903d8a17cf9d2adf16979bbde9c2b811bb331872fe80d96d3b67256f994b93954964889d33f0e8c9e00862d75f53d628ea07589fac05a4c7b22eecc1e8ba8712f0118ca48300a5cdc827c67fa7bad275700a91ad2274eb00d034ad0a6414aeeb85d533dd4cd3c9291b4eb1c59ea2b409d300e10212a1d299c15daa1f198c9d5541e8ce2e2d3582b91c8a7c910ed634513cb04f3377ab5b13df3f3f96d1078e7cfaf0a61981e71ff4d83d81ae52c4dec46a86c9e766a0fc5069a7aaca133851e643e39f895af3c09b2d7df184e6f973bb24ab186bb08f3ee7261998ce'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
mail=Mail(app)

from flaskblog import routes