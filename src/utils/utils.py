import pygame

from src.models.obstacles.snail.Snail import Snail
from src.models.obstacles.bat.Bat import Bat
from src.models.obstacles.grounder.Grounder import Grounder
from src.constants.paths import SNAIL_ANIMATION_1
from src.constants.paths import SNAIL_ANIMATION_2
from src.constants.paths import BAT_ANIMATION_1
from src.constants.paths import BAT_ANIMATION_2
from src.constants.paths import GROUNDER_ANIMATION_1
from src.constants.paths import GROUNDER_ANIMATION_2
from src.constants.paths import GROUNDER_ANIMATION_3
from src.constants.paths import GROUNDER_ANIMATION_4
from src.constants.paths import GROUNDER_ANIMATION_5
from src.constants.paths import GROUNDER_ANIMATION_6


def get_obstacle_by_type(type: str) -> Snail | Bat | Grounder:
    return {
        "snail": Snail(
            frames = [
                pygame.image.load(SNAIL_ANIMATION_1).convert_alpha(),
                pygame.image.load(SNAIL_ANIMATION_2).convert_alpha()
            ],
            y_pos = 300
        ),
        "bat": Bat(
            frames = [
                pygame.image.load(BAT_ANIMATION_1).convert_alpha(),
                pygame.image.load(BAT_ANIMATION_2).convert_alpha()
            ],
            y_pos = 210
        ),
        "grounder": Grounder(
            frames = [
                pygame.image.load(GROUNDER_ANIMATION_1).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_2).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_3).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_4).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_5).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_6).convert_alpha()
            ],
            y_pos = 300
        )
    }.get(type)

