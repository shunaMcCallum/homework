# Homework - Flask Calculator

#### Objectives

- Practice setting up and creating a Flask application

## Task

Your task is to create a simple calculator using Flask. This calculator should be able to add, subtract, multiply and divide two number. 

The user should be able to enter a URL containing the operation and the operands 

e.g. `http://127.0.0.1:5000/add/10/5`

And the answer should be displayed in the browser e.g.

`The answer is 15`


### Notes

1) Create a directory called `modules`.
Inside this directory create a file called `calculator.py`. This will contain the functions (`add`, `subtract`, `multiply`, `divide`) for your calculator.

You should make sure you test the functions in your `calculator.py` file, creating an appropriate test file.

2) Create an `app.py` file. This should contain the following code:

```python
from flask import Flask

app = Flask(__name__)
from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)
```    
    
3) Create a directory called `controllers`. Inside this folder create a file called `controller.py`. This file will contain the routes for your app. (Think about how many routes you will require)

Inside each route you will call the relevant function from the `calculator` module, passing it the route parameters passed in by the URL.

You will need to import the functions from the `calculator` module in this file.

Remember to import `app` in your `controller.py` file.

You may also want to create a `.flaskenv` file (refer to the classnotes for details).

**NOTE**: All arguments passed in the URL are passed as strings, so you will need to convert your operands to numbers.

**REMEMBER**
 
 - to create the `__init__.py` file in each directory. 
 - a `.gitignore` file



