from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from receive import message_listen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected!'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


def background_thread():
    def emit_message_callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        socketio.emit('my response',
                      {'data': body.decode('utf-8'), },
                      namespace='/test', broadcast=True)
    message_listen(emit_message_callback)


if __name__ == '__main__':
    socketio.start_background_task(target=background_thread)
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, use_reloader=False)
