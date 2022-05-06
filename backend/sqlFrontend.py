import sqlBackend
from flask import Flask, jsonify, request
app = Flask(__name__)

class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False

app.config.from_object(Config)

@app.route('/user/login', method=['GET', 'POST'])
def user_login():
    data = eval(request.data.decode())
    email = data.get('email')
    password = data.get('password')
    old_password, token = sqlBackend.login(email)
    if password == old_password:
        data = {"code": 20000, 'data': {"token": token}}
    else:
        data = {"code": 20001, 'msg': '密码错误'}
    return jsonify(data)

@app.route()
def test():
    pass
