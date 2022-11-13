# Space-Runner-Game-Program

## Getting Started

1. Clone repository in your computer
2. Access to correct path of your folder clone
3. Install virtual env, you can use: `virtualenv venv` in the console
4. Run `venv/Scripts/Activate` in your console
5. Install requirements.txt
6. Run `python new_main.py`
7. Enjoy

## Description

Space Runner is a game developed in Python through the Pygame library. In this game we are going to control a space runner who will try to dodge the targets that come towards him. The way to dodge will be using A, D and Space to jump, a and d to move laterally. As time goes by, it is counted as a score, survive more and you will have more points. We can also use different powers that will appear randomly on the visible field of the map.

## Technologies used

1. Python

## Libraries used

1. math
2. pygame
3. sys
4. random

## Galery

Game in progess. Description coming soon...

## Portfolio link

Game in progess. Description coming soon...

## Video

Game in progess. Description coming soon...

## Documentation

### new_main.py

---

`game_active` is a variable that will allow us to know if the user lost or is still playing, `start_time` is a variable that will help us to count the score since the game starts and `score` itself is the score of the player:

```
game_active = False
start_time = 0
score = 0
```

If you want to add some sound effect or a sound itself, all you have to do is call a variable with `pygame.mixer.Sound("YOUR_AUDIO")`, then we can use that variable to change the volume with `set_volume( )`, to play it `.play()` and to stop it `.stop()`:

```
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.1)

bg_music.play()
bg_music.stop()
```

What we see in these variables are `Groups` in which the sprites will be saved and we will be able to use these sprites to perform different types of actions. We have two types of `Groups`, we have the `GroupSingle()` that here a sprite will be saved only as the player or the power. Also if you look closely if we want to access the sprites to be able to handle them we use `.sprites()` and this will return a list of the sprites. We also have the `Group()` that refers to a group of Sprites here it is used for obstacles since we have more than one type of obstacle such as `snail, fly and grounder`:

```
player = pygame.sprite.GroupSingle()
player.add(Player())
character = player.sprites()[0]

power_coin = pygame.sprite.GroupSingle()

obstacle_group = pygame.sprite.Group()
```

The `display_score()` function will take care of returning the time elapsed since the game started in seconds.

The `collision_sprite()` function will take care of returning True or False depending on whether or not there was a collision. We will return these values ​​to modify `game_active` which is in charge of knowing if the game finished or not. If there was a collision and there are no powers activated that prevent these collisions, the function will return False, instead if there are no collisions or there are powers that prevent such collisions, the game will return True.

This way we can add fonts:

```
principal_font = pygame.font.Font("./font/Pixeltype.ttf", 50)
```

This way we can add images to render on what would be `screen`:

```
sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()
```

As we can see below there are different types of events and for each event there is a different timer. Both for sprite animations and for spawning a power on the map or obstacles:
Each `timer` will be passed the variable to apply the event for example `power_timer` and finally the time in which it will be executed, if we pass `5000` it will be executed after 5 seconds:

```
obstacle_timer = pygame.USEREVENT
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 500)

power_timer = pygame.USEREVENT + 4
pygame.time.set_timer(power_timer, randint(15000, 30000))
```

### Folder: audio

---

In the `audio` folder we will find all the audio or sounds that we use in the game.

### Folder: font

---

In the `font` folder we will find all the fonts that we use in the game.

### Folder: graphics

---

In the `graphics` folder we will find all the images that we use in the game.

### Folder: obstacle | obstacle.py

In the `obstacle` folder we will find an `obstacle.py` file in which the `Obstacle()` class is built.

The type of obstacle to create will be passed to this class, depending on the type different types of images will be rendered for that type of sprite, then they will be added to an array of frames to join them in an animation and the Y position of the obstacle will be modified:

```
if type == "fly":
    fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
    fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
    self.frames = [fly_frame_1, fly_frame_2]
    y_pos = 210
elif type == "snail":
    snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
    snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
    self.frames = [snail_frame_1, snail_frame_2]
    y_pos = 300
elif type == "grounder":
    grounder_frame_1 = pygame.image.load("graphics/Grounder/grounder1.png").convert_alpha()
    grounder_frame_2 = pygame.image.load("graphics/Grounder/grounder2.png").convert_alpha()
    grounder_frame_3 = pygame.image.load("graphics/Grounder/grounder3.png").convert_alpha()
    grounder_frame_4 = pygame.image.load("graphics/Grounder/grounder4.png").convert_alpha()
    grounder_frame_5 = pygame.image.load("graphics/Grounder/grounder5.png").convert_alpha()
    grounder_frame_6 = pygame.image.load("graphics/Grounder/grounder6.png").convert_alpha()
    self.frames = [grounder_frame_1, grounder_frame_2, grounder_frame_3, grounder_frame_4, grounder_frame_5, grounder_frame_6]
    y_pos = 300
```

The `animation_state()` method will handle the people animations using `frames` the list to go through for each image.

The `update()` method allows to check every second that passes in the game if some of the methods are fulfilled.

The `destroy()` method is in charge of destroying a sprite.

### Folder: player | player.py

In the `player` folder we will find an `player.py` file in which the `Player()` class is built.

The `Player()` class is very similar to the `Obstacle()` class but here only one type of player will be shown. In addition to the `Obstacle()` methods we can add:

The `player_input()` method is in charge of managing the player, that is to say, it is where we configure the keys to move the character. In synthesis that will happen every time that "X" key is touched.

The `apply_gravity()` method allows us to apply gravity on the character, that is to say, that there is gravity in the game.

The `limit_map()` method allows that the character does not leave the screen.

The `change_skin_player()` method allows that depending on the power that is grabbed the skin of the character changes or not to be able to differentiate the powers. If your skin changes to transparent is that you grabbed `immunity` on the other hand if your skin turns red you grabbed `killer`.

### Folder: power | power.py

In the `power` folder we will find an `power.py` file in which the `Power()` class is built.

The `Power()` class is very similar to the `Obstacle()` and `Player()` classes. In addition to the basic methods that `Obstacle()` and `Player()` have, we can add:

The `select_power()` method that will let us know which power was grabbed, depending on which power was activated, the corresponding variable will be set to True, from False to True:

```
self.immunity = False
self.killer = False
```

The `power_stop()` method allows us to modify when a seized power is going to end and return to normal.
