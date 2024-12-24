from flask import Flask,request,Response,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

if __name__ == "__main__":
    app.run(port=1234)