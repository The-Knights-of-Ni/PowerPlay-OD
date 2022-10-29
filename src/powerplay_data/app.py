from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return ''


@app.route("/data.zip")
def data():
    return send_file("data.zip")


if __name__ == "__main__":
    app.run(port=5000, debug=False)
