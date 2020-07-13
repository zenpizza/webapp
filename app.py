from flask import Flask, render_template, flash, redirect
import forms
from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/result/<answer>')
def result(answer):
    return render_template('result.html', answer=answer)

@app.route('/calc', methods=["GET", "POST"])
def doCalc():
    form = forms.CalcForm()
    if form.validate_on_submit():
        print(form.x.data * form.y.data)
        return redirect('/result/' + str(form.x.data * form.y.data))
    return render_template('calc.html', title='Calculator', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

app.run(host='0.0.0.0', port=8080, debug=True)