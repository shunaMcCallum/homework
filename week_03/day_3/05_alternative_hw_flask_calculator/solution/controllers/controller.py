from app import app
from modules import calculator

@app.route('/')
def index():
    return "Welcome to our calculator app!"

@app.route('/add/<num_1>/<num_2>')
def add(num_1, num_2):
    return f"The answer is {calculator.add(int(num_1),int(num_2))}"

@app.route('/subtract/<num_1>/<num_2>')
def subtract(num_1, num_2):
    return f"The answer is {calculator.subtract(int(num_1),int(num_2))}"

@app.route('/multiply/<num_1>/<num_2>')
def multiply(num_1, num_2):
    return f"The answer is {calculator.multiply(int(num_1),int(num_2))}"

@app.route('/divide/<num_1>/<num_2>')
def divide(num_1, num_2):
    return f"The answer is {calculator.divide(int(num_1),int(num_2))}"
