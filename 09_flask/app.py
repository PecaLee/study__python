from flask import Flask, render_template, request

app = Flask("minimalServer")


@app.route("/")
def home():
    args = request.args
    return render_template("home.html", args=args)
