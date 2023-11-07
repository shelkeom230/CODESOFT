from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]
results = {"rock": {"win": "scissors", "lose": "paper"},
           "paper": {"win": "rock", "lose": "scissors"},
           "scissors": {"win": "paper", "lose": "rock"}}

user_score = 0
computer_score = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    global user_score, computer_score

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif results[user_choice]['win'] == computer_choice:
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result,
                           user_score=user_score, computer_score=computer_score)


if __name__ == '__main__':
    app.run(debug=True)
