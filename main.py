from flask import Flask, request, render_template
from forms import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'antonio2023'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LcvkhQkAAAAAIZSjsjhh4MDj92Zy1MecXFodyEE'
app.config['RECAPTCHA_PRIVATE_KEY']='6LcvkhQkAAAAAOuzomA-tBNlHn7wJ-NMkWs5UTm_'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/form',methods=['GET','POST'])
def form():
    form = RegisterForm(request.form)
      
    if form.validate():
        msg = "La información es correcta"
        return render_template('form-back.html', msg = msg)

    #return render_template("register.html", form=form)
    return render_template('form-back.html', form=form)





app.run(host='0.0.0.0',port=5000, debug=True)