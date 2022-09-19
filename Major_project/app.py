# from flask import Flask
# from flask import render_template,redirect,jsonify,flash
# app=Flask(__name__)
# app.secret_Key="elixir"
# @app.route('/')
# def index():
#     return render_template('index.html')
# if __name__=="__main__":
#     app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
#froute
@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


  