from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/Route/", methods=['POST'])
def hello():
    return "Hello World!"