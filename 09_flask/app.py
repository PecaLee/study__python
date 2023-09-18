from flask import Flask

app = Flask("minimalServer")


@app.route("/")
def hello_world():
    return "hello world"
