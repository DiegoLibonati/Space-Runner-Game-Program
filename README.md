# Space Runner Game Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app`

## Description

Space Runner is a game developed in Python through the Pygame library. In this game we are going to control a space runner who will try to dodge the targets that come towards him. The way to dodge will be using A, D and Space to jump, a and d to move laterally. As time goes by, it is counted as a score, survive more and you will have more points. We can also use different powers that will appear randomly on the visible field of the map.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pygame
```

#### Requirements.test.txt

```
pytest
```

## Portfolio link

[`https://www.diegolibonati.com.ar/#/project/Space-Runner-Game-Program`](https://www.diegolibonati.com.ar/#/project/Space-Runner-Game-Program)

## Video

https://user-images.githubusercontent.com/99032604/201543320-020d09af-9266-4a0b-8fff-dbaf4083f587.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`