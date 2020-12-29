from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '8934y5uihkbjvfuyoiy4p3o85ugyihjvsb9a75bwefigu374tgf'
socketio = SocketIO(app)

@app.route('/')
def home():
	return render_template("index.html")

@socketio.on('message')
def message(data):
	send(data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
