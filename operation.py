from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
app = Flask(__name__)

cors = CORS(app)

@app.route('/add', methods=['GET'])
def addition():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));
    return f"additon of {num1} and {num2} is {num1 + num2}"

@app.route('/sub', methods=['POST'])
def substraction():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));
    return f"substraction of {num1} and {num2} is {num1 - num2}"

@app.route('/mul', methods=['PUT'])
def multiplication():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));
    return f"multiplication of {num1} and {num2} is {num1 * num2}"

@app.route('/div', methods=['DELETE'])
def division():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));
    return f"division of {num1} and {num2} is {num1 / num2}"

if __name__ == "__main__":
    app.run(debug=True)