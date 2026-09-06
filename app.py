from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello():
    message = os.getenv("APP_MESSAGE", "Hei fra Flask!")
    return f"<h1>{message}</h1><p>Servert fra miljøvariabel 🎉</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)