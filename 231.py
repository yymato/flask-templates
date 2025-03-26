from flask import request, render_template, url_for, redirect

from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def carousel():
    if request.method == 'GET':
        data = [url_for('static', filename=f'img/{i}') for i in os.listdir('static/img')]
        return render_template('f.html', data=data)
    elif request.method == 'POST':
        f = request.files['file']
        print(f)
        last_index = int(max(os.listdir('static/img')).split('.')[0])
        with open(f'static/img/{last_index + 1}.jpg', mode='wb') as pict:
            pict.write(f.read())
        return redirect('/')



if __name__ == '__main__':
    app.run()