from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/RouteHerePost/", methods=['POST'])
def hello2():
    return "Hello World! (POST)"
	
@app.route("/RouteHereGet/", methods=['GET'])
def hello3():
    return "Hello World! (GET)"