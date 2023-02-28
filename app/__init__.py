# !!START
from flask import Flask,render_template,redirect
from .config import Config
from .tweets import tweets
from .form.form import CreateTweet
from random import randint
from datetime import date

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
    sortedTweets = sorted(tweets, key=lambda tweet: tweet['date'], reverse=True)
    return render_template('feed.html', tweets=sortedTweets)

@app.route('/new', methods=["GET","POST"])
def create_tweet():

    form=CreateTweet()
    if form.validate_on_submit():
        new_tweet={
            'id':len(tweets)+1,
            "author":form.data['author'],
            'tweet':form.data['tweet'],
            'likes':0,
            "date": str(date.today().strftime("%d/%m/%Y"))
        }
        print(new_tweet)
        tweets.append(new_tweet)
        return redirect('/feed')
    if form.errors:
        print(form.errors)
        return render_template('new_tweet.html', form=form, errors=form.errors)
    return render_template('new_tweet.html', form=form, errors=None)
