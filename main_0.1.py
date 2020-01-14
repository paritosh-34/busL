from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['MONGO_URI'] = 'mongodb://localhost/busL'
mongo = PyMongo(app)


@app.route('/api/test')
def test_api():
    return jsonify({"about": "Hello World"})


@app.route('/api/latlon', methods=['GET', 'POST'])
def latlon():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
    if request.method == 'GET':
        pass

    return 201


@app.route('/api/nfc', methods=['GET', 'POST'])
def nfc():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
    return 201


if __name__ == '__main__':
    app.run()