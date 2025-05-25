from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Over 5 billion people worldwide use social media",
              "Individuals spend an average of 2 hours and 20 minutes daily on social media",
              "Facebook, YouTube, and WhatsApp are among the most popular social media platforms, with millions of monthly active users,"
              "A large portion of social media users are under 35 years old, with platforms like Instagram particularly popular with younger demographics",
              "Social commerce, where purchases are made directly within social media platforms, is on the rise"]

@app.route("/")
def hello_world():
    return '<p>Hello World</p>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin")
def coin():
    coin = random.randint(0, 1)
    message = ""
    if coin == 1:
        message = "tails"
    else:
        message = "face"

    return f'<p>{message}</p>'

app.run(debug=True)
