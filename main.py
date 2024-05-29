from flask import Flask,render_template,url_for,redirect,request
import os
import requests
import json
import random

app=Flask(__name__)

def get_meme(channel):
    sr=channel
    url="https://meme-api.com/gimme/"+sr 
    response=json.loads(requests.request("GET",url).text)  
    meme_large=response["preview"][-1]
    subreddit=response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def callMeX():  
    img_dir = os.path.join(app.static_folder, 'images') 
    images = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]  
    descriptions_path = os.path.join(os.path.dirname(__file__), 'images.json')
    with open(descriptions_path, 'r') as f:
        descriptions = json.load(f)
    selected_image = random.choice(images)
    description = descriptions.get(selected_image, "Lund mera") 

    image_data = {
        'url': url_for('static', filename=f'images/{selected_image}'),
        'description': description
    }  
    return render_template('indra.html', image_data=image_data)
 
@app.route('/navigate', methods=['POST'])
def navigate(): 
    variable_name = request.form['variable_name']  
    return redirect(f'/{variable_name}')


@app.route("/<channel>")
def index(channel):
    meme_pic,subreddit=get_meme(channel)
    return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit)

if __name__=='__main__':
    app.run(debug=True)
