from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
