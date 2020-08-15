#--------Flask Hello World----------#
#import the flask class from the flask package
from flask import Flask

#create the application object
app = Flask(__name__)
app.config["DEBUG"]= True

#use the decorator pattern to link 
#the view function to  a url

#define the view using a function , which return a string 
@app.route("/")
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return  "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "naveen":
        return "hello, {}".format(name), 200
    else:
        return "not found", 404


#start development server using the run() method
if __name__ == "__main__":
    app.run()
    