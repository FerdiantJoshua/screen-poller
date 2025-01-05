# app.py
from io import BytesIO
import os
import signal
import time

from flask import Flask, request, send_file, send_from_directory
from PIL import Image  # we need to import this to allow pyautogui.screenshot() to work
import pyautogui

PID = os.getpid()
app = Flask(__name__)

import os 
@app.route('/')
def health_check():
    return {'status': 'healthy', 'path': os.path.dirname(os.path.realpath(__file__)), 'timestamp': time.time()}

@app.route('/pollScreen')
def get_screenshot():
    # Take screenshot
    screenshot = pyautogui.screenshot()
    
    # Convert to bytes
    img_byte_arr = BytesIO()
    screenshot.save(img_byte_arr, format='WEBP', quality=50)
    img_byte_arr.seek(0)
    
    return send_file(
        img_byte_arr,
        mimetype='image/webp',
        as_attachment=False
    )

@app.route('/viewer')
def viewer():
    return send_from_directory('./', 'index.html')

@app.route('/shutdown')
def shutdown():
    # this mimics a CTRL+C hit by sending SIGINT
    # it ends the app run, but not the main thread
    pid = os.getpid()
    assert pid == PID
    os.kill(pid, signal.SIGINT)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
