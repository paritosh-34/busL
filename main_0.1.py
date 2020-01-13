from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api/test')
def test_api():
    return jsonify({"about": "Hello World"})


@app.route('/api/latlon', methods=['GET', 'POST'])
def latlon():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
    return "ok"


if __name__ == '__main__':
    app.run()