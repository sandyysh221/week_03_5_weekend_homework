from flask import Flask

app = Flask(__name__)

from controllers import controller

if __name__ == "__main)__":
    app.run(debug=True)
