from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2


app = Flask(__name__, template_folder='application/templates')
app = Flask(__name__, template_folder='./')


@app.route('/')
def home():
    return render_template('simple.html')


socketio = SocketIO(app, async_mode=None, cors_allowed_origins="*", manage_session=False, logger=False, debug=False)


@socketio.on('connect')
def handle_connect():
    print('CONNECTED')
    socketio.emit('send data')


def messageReceived():
    ret = True
    cap = cv2.VideoCapture('./test.mp4')

    while ret:
        ret, frame1 = cap.read()
        frame = cv2.imencode('.jpg', frame1)[1]
        frame = frame.tobytes()

        print('message received!!!')
        socketio.emit('my response', frame)
        socketio.sleep(0)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    messageReceived()


def gen(video_path):
    video = cv2.VideoCapture(video_path)
    frame, ret = video.read()

    while ret:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/api/feed')
def feed_frames():
    video_path = './test.mp4'
    return Response(gen(video_path), mimetype='multipart/x-mixed-replace; boundary=frame')



def ack(value):
    if value != 'pong':
        raise ValueError('unexpected return value')

@app.route('/ping')
def ping():
    socketio.emit('ping event', {'data': 42}, namespace='/ping')

if __name__ =='__main__':
    socketio.run(app)
