
from flask import Flask
app = Flask(__name__)
app.debug = True # for development, not when you put on the real internet

@app.route('/lecture/on/<day>')
def hello_user(day):
    return '<h1>its {0} !</h1>'.format(day)

if __name__ == '__main__':
    app.run()