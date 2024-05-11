import urllib.parse
from flask import Flask,request,Response,session,render_template,jsonify
from functools import wraps
from config import secret
import urllib,os,base64

app = Flask(__name__)
app.secret_key=secret.encode()

Flag = open("flag.txt","rb").read()
blacklist = ["config.py","app.py","flag"]
def authenticated(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "role" not in session:
            return "Unauthorized", 401  # Return unauthorized status code
        if session.get("role")!="admin":
            return "You are not admin"
        return func(*args, **kwargs)
    return decorated_function
@app.route("/",methods=["GET"])
def index():
    session['role']="user"
    return render_template("index.html",data="kon")

@app.route("/readfile",methods=["GET"])
def readfile():
    file = request.args.get("file")
    for i in blacklist:
        if i in file:
            return "Mother fucker"
    fo = open(file,"rb")
    return fo.read().decode("utf-8")
@app.route("/login",methods=["GET"])
@authenticated
def login():
    return Flag
if __name__ == "__main__":
    app.run(port="1234",debug=True)
