from flask import Flask, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'value': 'Hello World'})