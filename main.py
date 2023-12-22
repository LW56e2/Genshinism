from flask import Flask, request, render_template, redirect, flash, session
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
autoHostIP = s.getsockname()[0]
s.close()

print(autoHostIP)
hostIp = autoHostIP
port = '8001'
hostPort = hostIp + ':' + port
site = 'http://' + hostPort

app = Flask(__name__)

app.secret_key = ''

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8001)