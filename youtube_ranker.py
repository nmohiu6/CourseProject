from flask import Flask, render_template, request
from rank import getRankedURLs
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    # extract_name = request.form.get("name")
    query = request.form.get("query")
    titles = getRankedURLs(query)
    return render_template('index.html', titles=titles)