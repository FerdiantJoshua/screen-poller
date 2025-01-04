# app.py
import time
from io import BytesIO

from flask import Flask, send_file, send_from_directory
from PIL import Image
import pyautogui

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
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return send_file(
        img_byte_arr,
        mimetype='image/png',
        as_attachment=False
    )

@app.route('/viewer')
def viewer():
    return send_from_directory('./', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
