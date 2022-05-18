from app import app
from flask import render_template
from models.orders import orders

@app.route('/')
def index():
    return "Welcome to the Book Shop"

@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Home Page", orders=orders)

@app.route('/orders/<index>')
def get_single_order(index):
    return render_template('order.html', title="Orders", orders=orders, index=index)


