from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    extract_name = request.form.get("name")
    name = "My name is " + request.form.get("name")
    return render_template('index.html', name=name)