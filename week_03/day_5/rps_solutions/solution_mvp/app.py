from flask import Flask

app = Flask(__name__)

from controllers import game_controller

if __name__ == "__main__":
    app.run(debug=True)