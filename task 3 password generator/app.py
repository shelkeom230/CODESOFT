from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
