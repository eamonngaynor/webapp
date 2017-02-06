
from flask import Flask 

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_func() -> str:
  
    return 'Hello from my first web app.'

@app.route('/bye')
def byebye() -> str:
    return 'So long and thanks for all the fish'



@app.route('/input/<first>/<last>')
def display_name(first: str, last: str) -> str:
    return 'Hello,' +str(first) + '' + str(last)




if __name__== '--main--':
    app.run(debug = True)
