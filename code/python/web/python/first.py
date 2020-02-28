from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<qqq>')
def hello_world(qqq):
   return render_template("hello.html")
@app.route('/')
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug=True)