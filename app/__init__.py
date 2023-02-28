# !!START
from flask import Flask,render_template
from .config import Config
from .tweets import tweets
from random import randint

app = Flask(__name__)

app.config.from_object(Config)
# !!END
@app.route('/')
def home():
    randInt=randint(0,4)
    tweet=tweets[randInt]
    return render_template('index.html', tweet=tweet)

@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)