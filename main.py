from flask import Flask, flash, render_template, request
from requests import get
from keys import api_key
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        city = request.form['searchcity']
        res = get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
        if res.status_code != 200:
            flash(f'Can\'t show {city}', 'danger')
            return render_template('home.html')
        return render_template('result.html', response=res)
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = 'shah1234'
    app.run(debug=True)