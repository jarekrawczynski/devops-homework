from flask import Flask, request

app = Flask(__name__)

@app.route('/',endpoint='/', methods=["GET"] )
@app.route('/healthz',endpoint='healthz', methods=["GET"])
def hello_world():
    
    if request.endpoint == '/':
    	msg = 'backend 2 !!!!!!!!\n'
    elif request.endpoint == 'healthz':
    	msg = ''

    return msg