from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '76b7dbec0285b9d18cee5f2902c4677f'

posts = [
    {
        'author':'Anders Selborn',
        'title' : 'Meningen med livet',
        'content': 'En meningsfull bok',
        'date_posted': '19 april 2023'
    },

    {
        'author':'Anders Selborn',
        'title' : 'Meningen med att andas',
        'content': 'En meningslös bok',
        'date_posted': '19 april 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.debug = True
    app.run() 
