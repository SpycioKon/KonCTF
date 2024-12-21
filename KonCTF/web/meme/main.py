from flask import Flask,render_template,request,session,flash,url_for,redirect,get_flashed_messages
from werkzeug.security import generate_password_hash,check_password_hash
import os
from config import UPLOAD_FOLDER,check_authenticated,ALLOWED_COMMANDS,COMMAND_PATTERN
import re
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)        

Users = {}

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in Users and check_password_hash(Users[username],password):
            flash("Login OK")
            session['username'] = username
            return redirect(url_for("admin"))
        else:
            flash("Nguoi dung khong hop le")
            return redirect(url_for("login"))
    else:
        return render_template('login.html')
@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in Users:
            flash("User da ton")
            return redirect(url_for('register'))
        else:
            Users[username] = generate_password_hash(username)
            session['username'] = username
            return redirect(url_for("admin"))
    else:
        return render_template("register.html")
@app.route("/logout",methods=["GET"])
def logout():
    flash("Ban da logout")
    session.pop('username',None)
    return redirect(url_for('login'))
@app.route("/admin",methods=["GET","POST"])
def admin():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(url_for("admin"))
        else:
            files = request.files['file']
            files.save(os.path.join(UPLOAD_FOLDER,files.filename)) # yeah, my friend cant execute php code so he cant rce right?? 
            flash("da upload thanh cong")
    return render_template('admin.html')

@app.route('/shell', methods=['GET'])
def shell():
    command = request.args.get('command')
    
    if command is None:
        return "No command provided."
    
    parts = command.split()
    base_command = parts[0]
    
    if base_command in ALLOWED_COMMANDS and re.match(COMMAND_PATTERN, command):
        result = subprocess.run(parts, capture_output=True, text=True)
        return result.stdout
    else:
        return f"Command '{command}' is not allowed or contains invalid characters."

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=1234,debug=True)