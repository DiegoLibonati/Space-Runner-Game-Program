import pygame

from src.models.obstacles.obstacle import Obstacle


class Bat(Obstacle):
    def __init__(self, frames: pygame.Surface, y_pos: int) -> None:
        super().__init__(frames=frames, y_pos=y_pos)

    def config(self) -> None:
        pass
