from flask import Flask, render_template
from python.web.page_mapping import page_mapping

app = Flask(__name__)

page_mapping(app)

@app.route('/hello/<qqq>')
def hello_world(qqq):
   return render_template("hello.html")


if __name__ == '__main__':
   app.run(debug=True)
