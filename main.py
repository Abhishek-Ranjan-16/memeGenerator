from flask import Flask,render_template
import requests
import json

app=Flask(__name__)

def get_meme(channel):
    sr=channel
    url="https://meme-api.com/gimme/"+sr
    # url="https://meme-api.com/gimme"
    # jab bhi kuch api fetch krna toh iss tarah seh fetch krlena
    response=json.loads(requests.request("GET",url).text) # yaha meh conversion chal rha hai json ka shayad

    # yeh niche wala structure ke hisab seh select hua hai apne aap
    meme_large=response["preview"][-1]
    subreddit=response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def callMeX(): 
    return render_template("indra.html")
@app.route("/<channel>")
def index(channel):
    meme_pic,subreddit=get_meme(channel)
    return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit)

app.run(debug=True)
