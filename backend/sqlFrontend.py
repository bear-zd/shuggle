import sqlBackend
from flask import Flask, jsonify, request
app = Flask(__name__)

class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False

app.config.from_object(Config)

@app.route('/login', method=['GET', 'POST'])
def user_login():
    data = eval(request.data.decode())
    email = data.get('email')
    password = data.get('password')
    user_password, userid, email = sqlBackend.login(email)[0]
    if password == user_password:
        data = {"code": 20000, 'data': {"userid": userid, "email":email}}
    else:
        data = {"code": 20001, 'msg': '密码错误'}
    return jsonify(data)

@app.route()
def test():
    pass

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 11090)