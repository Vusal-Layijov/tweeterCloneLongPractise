# !!START
from flask import Flask,render_template
from .config import Config
from .tweets import tweets
from .form.form import CreateTweet
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

@app.route('/new')
def create_tweet():
    form=CreateTweet()
    return render_template('new_tweet.html', form=form)
