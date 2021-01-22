from flask import Flask, render_template
from weather import get_weather, URL
from datetime import datetime
from flask import request



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('пришел POST-запрос')
        print('-' * 80)
        print(request)
    print('пришел GET-запрос')
    if request:
        print(request.form, request, dict(request.form))
    else:
        print('error')
    return render_template('index.html', weather=get_weather('Moscow'), page_var=str(datetime.now()))


if __name__ == '__main__':
    app.run(debug=True)
