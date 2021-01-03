import os
from flask import Flask, render_template, redirect, session, request, url_for
from flask_socketio import SocketIO, send, emit

#4.3.2

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')
socketio = SocketIO(app)


@app.route('/', methods = ['GET', 'POST'])
def username():
	#if the user presses the submit button on username screen
	if request.method == "POST":
		username = request.form["usr"]
		session["username"] = username
		if session["username"] != "":
			return redirect(url_for("home"))
	return render_template("username.html")

@app.route('/home')
def home():
	return render_template("home.html", username=session["username"])

#@app.route("/audio_stream")
#def Audio_Stream():
    #r = requests.get("http://localhost:8082/audio_stream.mp3", stream=True)
    #return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')

@socketio.on('message')
def message(data):
	print(data)
	emit("message", data, broadcast = True)
	
	


if __name__ == '__main__':
    app.run()
