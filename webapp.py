
from flask import Flask 

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_func() -> str:
  
    return 'Hello from my first web app.'

@app.route('/bye')
def byebye() -> str:
    return 'So long and thanks for all the fish'


if __name__== '__main__':
    app.run(debug = True)
