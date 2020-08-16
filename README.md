# socketio-flask-video-stream
Video Streaming on flask using two methods sending video frame by frame or send using socket events


<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/harshavkumar/socketio-flask-video-stream.git
$ cd socketio-flask-video-stream
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$
$ # Another thing we have use is ngrok (testing purpose) to broadcast socetio on https
$ # you have to change simple.html script connection link with your own nrok generated link on flask deployed URL
$
$ # Start the application
$ (Windows) waitress-serve --port=8001 simple:app
$ (Unix/Mac) gunicorn --bind 0.0.0.0:8001 simple:app
$
$ # Access the feed in browser: http://127.0.0.1:5000/
$ # and also check browser console status 
```
