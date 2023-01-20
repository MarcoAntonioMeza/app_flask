
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



app.run(host='0.0.0.0',port=5000, debug=True)