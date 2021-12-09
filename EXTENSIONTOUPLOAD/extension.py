from flask import Flask, render_template, request
from rank import getRankedURLs 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/user', methods=['POST'])
def user():
    query = request.form.get("search_box")
    results = getRankedURLs(query)
    return render_template('popup.html', results=results)