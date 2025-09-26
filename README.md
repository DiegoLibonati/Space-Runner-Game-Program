# Space Runner Game Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app`

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Space Runner is a game developed in Python through the Pygame library. In this game we are going to control a space runner who will try to dodge the targets that come towards him. The way to dodge will be using A, D and Space to jump, a and d to move laterally. As time goes by, it is counted as a score, survive more and you will have more points. We can also use different powers that will appear randomly on the visible field of the map.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pygame==2.6.1
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio link

[`https://www.diegolibonati.com.ar/#/project/Space-Runner-Game-Program`](https://www.diegolibonati.com.ar/#/project/Space-Runner-Game-Program)

## Video

https://user-images.githubusercontent.com/99032604/201543320-020d09af-9266-4a0b-8fff-dbaf4083f587.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Join to the correct path of the clone
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec"`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Join to the correct path of the clone
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed src/app.py`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues
