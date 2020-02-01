from flask import Flask, jsonify, request, render_template, session, redirect
# from flask_mysqldb import MySQL
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.secret_key = "super-secret-key"
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'busL'

app.config['MONGO_URI'] = 'mongodb://localhost/busL'
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user' in session:
        return "Welcome "+session['user']+"!" + "<br>" + '''<a href="/logout">Logout</a>'''

    if request.method == 'POST':
        username = request.form.get('email')
        userpass = request.form.get('pass')
        print(username)
        print(userpass)
        re = mongo.db.users.find_one({"name": username, "pass": userpass})
        print(re)
        if re is None:
            return "False"
        else:
            session['user'] = username
            return "True"

    return render_template('login.html')


@app.route('/mlogin', methods=['GET', 'POST'])
def mlogin():
    if request.method == 'POST':
        content = request.data
        print(type(content))
        print(content)
#         email = content['email']
#         password = content['password']
#         flag = content['flag']
#         fcm_token = content['fcm_token']
#         re = mongo.db.users.find_one({"name": email, "pass": password})

#         print(re)
#         if re is None:
#             data = {
#                 "value": 0,
#                 "message": "not ok",
#                 "email": email,
#                 "name": email,
#                 "id": "123"
#             }
#             y = json.dumps(data)
#             return y
#         else:
#             # session['user'] = username
#             data = {
#                 "value": 1,
#                 "message": "ok",
#                 "email": email,
#                 "name": email,
#                 "id": "123"
#             }
#             y = json.dumps(data)
#             return y
    return "wrong method"


@app.route('/locs')
def locations():
    if 'user' in session and session['user'] == "admin@gmail.com":
        result = mongo.db.location.find()
        list_r = list(result)
        return render_template('home.html', posts=list_r)
    return "abort"


@app.route('/api/test')
def test_api():
    return jsonify({"about": "Hello World"})


@app.route('/post', methods=['GET', 'POST'])
def latlon():
    if request.method == 'POST':
        content = request.get_json()
        # z = json.loads(content)
        lat = content['lat']  # flag, email, password, fcm_token
        lon = content['lon']
        mongo.db.location.insert({'lat': lat, 'lon': lon})
        data = {
                "temp" : "tempC",
                "time" : "timee"
            }
        y = json.dumps(data)
        return y
    return "method not allowed"
#     return "Not a valid method"


@app.route('/buses')
def buses():
    result = mongo.db.seats.find()
    list_r = list(result)
    print(list_r)
    return render_template('bus.html', posts=list_r)


@app.route('/cbuses', methods=['GET', 'POST'])
def cbuses():
    if 'user' in session and (session['user'] == "cd1@gmail.com" or session['user'] == "admin@gmail.com"):
        if request.method == 'POST':
            re = request.get_json()
            print(type(re))
            print("-->", re)

            for i in re:
                print(i, re[i])
                mongo.db.seats.update({'no': i}, {'info': re[i]})

        result = mongo.db.seats.find()
        list_r = list(result)
        print(list_r)
        return render_template('busC.html', posts=list_r)
    else:
        return "Not Allowed"


@app.route('/cbuses/r', methods=['GET', 'POST'])
def Rcbuses():
    if 'user' in session and (session['user'] == "cd1@gmail.com" or session['user'] == "admin@gmail.com"):
        if request.method == 'POST':
            re = request.get_json()
            print(type(re))
            print("-->", re)

            for i in re:
                print(i, re[i])
                mongo.db.seats.update({'no': i}, {'info': re[i]})

        result = mongo.db.seats.find()
        list_r = list(result)
        print(list_r)
        return render_template('busC2.html', posts=list_r)
    else:
        return "Not Allowed"


@app.route('/map')
def map():
    return render_template('index3.html')


@app.route('/set')
def set():
    return render_template('conductor.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
