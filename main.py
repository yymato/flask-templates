import json

from flask import Flask, url_for, render_template
import flask


app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
