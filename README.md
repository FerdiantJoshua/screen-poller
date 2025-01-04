# Screenshot Poll

A Python-based server to serve sending a periodical screenshots. This can be used to share a screen live without explicitly showing that we're screen-sharing. Although, as this program is unoptimized, this still consumes lots of bandwidth (around 2 Mbps) due to sending periodic full-screen-sized images.

## Requirements

Python 3.10

```sh
python -m venv venv
# Windows
.\venv\Scripts\activate.bat
pip install -r requirements.txt
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

## Building into A No-console Executable

Create a windowless executable, so that the server can be run without any visual trace, therefore becoming invisible when screen sharing.

```sh
pyinstaller --onefile --noconsole ./main.py
.\dist\main.exe
```

To terminate, go to Process/Task Manager, and look for `main.exe`, then terminate manually.

### Additional Instructions

In Windows, the app will have path in `C:\<username>\AppData\Local\Temp\_MeiXXXXXX`.  
You'll need to copy the `index.html` into the correct path so that the `/viewer` endpoint works.

1. Access `/` (root) to get the path
2. Copy the `index.html` to the path in the Local\Temp
3. Sometimes, you need to adjust the permission, to add Read permission to `Everyone`

## Author

Ferdiant Joshua Muis

_P.S. this app is mostly created by Claude. I just modify some part of it._
