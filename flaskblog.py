from flask import Flask,render_template,url_for
app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)