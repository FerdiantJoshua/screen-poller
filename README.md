# Screenshot Poll

A Python-based server to serve sending a periodical screenshots. This can be used to share a screen live without explicitly showing that we're screen-sharing. Note that, as this program is unoptimized, this still consumes lots of bandwidth (around 2 Mbps) due to sending periodic full-screen-sized images. I've used WEBP to compress the image, but it still may be quite computational & bandwidth-hungry.

## Requirements

Python 3.10

```sh
python -m venv venv
# Windows
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Linux

On Linux Ubuntu 22.04.4 LTS, you need to install these dependencies too:

```sh
sudo apt-get install python3-tk python3-dev  # this is for pyautogui to work
sudo apt install gnome-screenshot  # this is for Pillow to work
```

## Usage

### Development Mode

```sh
python main.py
```

### Production Mode

```sh
waitress-serve --host 0.0.0.0 --port 5000 main:app
```

Access the server in `localhost:5000`.

### Available Endpoints

1. `/` (root)  
    For health check, and other metadata

2. `/pollScreen`  
    The main pollscreen API

3. `/viewer`  
    The GUI version, to help polling the screenshot periodically, and also support partial screenshot.

4. `/shutdown`
    Terminate the server gracefully.

## Building into A No-console Executable

Create a windowless executable, so that the server can be run without any visual trace, therefore becoming invisible when screen sharing.

```sh
pyinstaller --add-data "./index.html:." --onefile --noconsole ./main.py
.\dist\main.exe
```

To terminate, go to Process/Task Manager, and look for `main.exe`, then terminate manually.

## Author

Ferdiant Joshua Muis

_P.S. this app is mostly created by Claude. I just modify some part of it._
