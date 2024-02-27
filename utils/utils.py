import pygame

def obstacle_structure() -> dict:
    return {
        "fly": {
            "frames": [
                pygame.image.load("graphics/fly/fly1.png").convert_alpha(),
                pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            ],
            "y_pos": 210
        },
        "snail": {
            "frames": [
                pygame.image.load("graphics/snail/snail1.png").convert_alpha(),
                pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            ],
            "y_pos": 300
        },
        "grounder": {
            "frames": [
                pygame.image.load("graphics/Grounder/grounder1.png").convert_alpha(),
                pygame.image.load("graphics/Grounder/grounder2.png").convert_alpha(),
                pygame.image.load("graphics/Grounder/grounder3.png").convert_alpha(),
                pygame.image.load("graphics/Grounder/grounder4.png").convert_alpha(),
                pygame.image.load("graphics/Grounder/grounder5.png").convert_alpha(),
                pygame.image.load("graphics/Grounder/grounder6.png").convert_alpha()
            ],
            "y_pos": 300
        }
    }


def player_structure() -> dict:
    return {
        "frames": [
            pygame.image.load("graphics/player/player_walk_1.png").convert_alpha(),
            pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        ],
        "jump_frame": pygame.image.load("graphics/player/jump.png").convert_alpha(),
        "jump_sound": pygame.mixer.Sound("audio/jump.mp3"),
        "y_pos": 210
    }


def power_structure() -> dict:
    return {
        "frames": [
            pygame.image.load("graphics/PowerCoin/mistery1.png").convert_alpha(),
            pygame.image.load("graphics/PowerCoin/mistery2.png").convert_alpha(),
            pygame.image.load("graphics/PowerCoin/mistery3.png").convert_alpha(),
            pygame.image.load("graphics/PowerCoin/mistery4.png").convert_alpha(),
            pygame.image.load("graphics/PowerCoin/mistery5.png").convert_alpha(),
            pygame.image.load("graphics/PowerCoin/mistery6.png").convert_alpha()
        ],
        "power_sound": pygame.mixer.Sound("audio/powerup.mp3"),
        "y_pos": 300
    }
 

def get_obstacle_type(
    type: str
) -> dict:
    return obstacle_structure().get(type)

