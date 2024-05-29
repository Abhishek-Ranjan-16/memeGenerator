from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Drink more coffee RIGHT NOW!!"

app.run()

