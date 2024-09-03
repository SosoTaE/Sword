from flask import render_template

def home_route():
    return render_template("index.html")