from flask import Flask, render_template

# IMPORT CONTROLLERS HERE
from controllers.member_controller import members_blueprint

app = Flask(__name__)

# REGISTER BLUEPRINTS HERE
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    