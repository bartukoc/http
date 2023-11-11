from flask import Flask
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<h1>merhaba<h1><a href='/rastgele_gercek'>link</a>"


@app.route("/rastgele_gercek")
def rasgele():
    liste = ["elon musk 54 yasinda", "Elon musk twitterin sahibidir"]

    x = random.choice(liste)

    return f'<h1>{x}</h1>'


app.run(debug=True)
