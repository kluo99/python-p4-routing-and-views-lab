#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:string>")
def print_string(string):
    print(string)
    return string

@app.route("/count/<int:num>")
def count(num):
    result = ""
    for i in range(1, num + 1):
        result += str(i) + "\n"
        # return i
    return result

@app.route("/math/<int:num1>/<operator>/<int:num2>")  
def math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == "div":
        return str(num1 / num2)
    elif operator == "%":
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
