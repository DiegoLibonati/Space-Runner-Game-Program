import pygame

from src.core.paths import (
    BAT_ANIMATION_1,
    BAT_ANIMATION_2,
    GROUNDER_ANIMATION_1,
    GROUNDER_ANIMATION_2,
    GROUNDER_ANIMATION_3,
    GROUNDER_ANIMATION_4,
    GROUNDER_ANIMATION_5,
    GROUNDER_ANIMATION_6,
    SNAIL_ANIMATION_1,
    SNAIL_ANIMATION_2,
)
from src.models.obstacles import Bat, Grounder, Snail


def get_obstacle_by_type(type: str) -> Snail | Bat | Grounder:
    return {
        "snail": Snail(
            frames=[
                pygame.image.load(SNAIL_ANIMATION_1).convert_alpha(),
                pygame.image.load(SNAIL_ANIMATION_2).convert_alpha(),
            ],
            y_pos=300,
        ),
        "bat": Bat(
            frames=[
                pygame.image.load(BAT_ANIMATION_1).convert_alpha(),
                pygame.image.load(BAT_ANIMATION_2).convert_alpha(),
            ],
            y_pos=210,
        ),
        "grounder": Grounder(
            frames=[
                pygame.image.load(GROUNDER_ANIMATION_1).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_2).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_3).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_4).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_5).convert_alpha(),
                pygame.image.load(GROUNDER_ANIMATION_6).convert_alpha(),
            ],
            y_pos=300,
        ),
    }.get(type)
