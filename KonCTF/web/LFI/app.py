from flask import Flask,Response, render_template,request
import os
import re
import pathlib
import subprocess

app = Flask(__name__)
def check(url):
    if re.match('\.\./',url):
        return True
    return False

@app.route("/",methods=["GET"])
def index():
    url = request.args.get('url')
    result = ""
    try:
        if check(url):
            result = "Cant exploit me!! "
        else:
            peak = os.getcwd().replace(" ","%20")
            cmd = f"curl file://{peak}/templates/{url}" #../flag.txt
            ans = subprocess.check_output(["curl", f"file://{peak}/templates/{url}"], text=True)
            result = ans
    except:
        result = "Somthing error!!"
    return render_template("index.html",result=result)
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=1234,debug=True)