from flask import Flask, render_template, request

app = Flask("minimalServer")


@app.route("/")
def home():
    listing_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render_template("home.html", args=listing_num)
