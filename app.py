from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hei fra Flask!</h1><p>Servert fra mitt virtuelle miljø 🎉</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)