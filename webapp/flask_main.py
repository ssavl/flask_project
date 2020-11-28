from flask import Flask, render_template
from weather import get_weather, URL
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', weather=get_weather('Moscow'), page_var=str(datetime.now()))


if __name__ == '__main__':
    app.run(debug=True)
