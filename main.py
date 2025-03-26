import json

from flask import Flask, url_for, render_template
import flask

from forms.login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)

@app.route('/training/<param>')
def training_flight(param):
    return render_template('training_in_flight.html', param=param)

@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_of_professions.html', list=lst, list_prof=professions)

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        'фамилия': '1',
        'имя': '2'
    } # Шаблон сделан через цикл, так что количество параметров может быть любым
    return render_template('auto_answer.html', data=data.items())

@app.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>success</h1>'

    return render_template('login.html', form=form)

@app.route('/distribution')
def distribution():
    data = ['User1', 'User2', 'User3', 'User4']
    return render_template('cabin.html', data=data)

@app.route('/table/<string:sex>/<int:age>')
def table(sex, age):
    if sex == 'male':
        if age > 21:
            color = '#0000FF'
            picture = url_for('static', filename='img/man_picture.png')
        else:
            color = '#AFEEEE'
            picture = url_for('static', filename='img/child_picture.png')
    else:
        if age > 21:
            color = '#FF4500'
            picture = url_for('static', filename='img/fem_picture.png')
        else:
            color = '#FF6347'
            picture = url_for('static', filename='img/child_picture.png')

    return render_template('picture_cabin.html', color=color, image=picture)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
