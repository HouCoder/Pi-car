from flask import Flask
from flask import render_template
import RPi.GPIO as gpio

app = Flask(__name__)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)

def backward():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)

def left():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)

def right():
    init()
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)

def stop():
    gpio.cleanup()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/forward')
def go_forward():
    forward()
    return 'True'

@app.route('/backward')
def go_backward():
    backward()
    return 'True'

@app.route('/left')
def go_left():
    left()
    return 'True'

@app.route('/right')
def go_right():
    right()
    return 'True'

@app.route('/stop')
def go_stop():
    stop()
    return 'True'

if __name__ == "__main__":
    print "Start"
    app.run(host='0.0.0.0',port=5010)
