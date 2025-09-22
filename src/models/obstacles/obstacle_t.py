from abc import ABC
from abc import abstractmethod
from random import randint

import pygame 


class Obstacle(pygame.sprite.Sprite, ABC):
    def __init__(self, frames: list[pygame.Surface], y_pos: int) -> None:
        super().__init__()

        self._frames: list[pygame.Surface] = frames
        self._y_pos: int = y_pos

        self._animation_index: int = 0

        self.image: pygame.Surface = self._frames[self._animation_index]
        self.rect: pygame.Rect = self.image.get_rect(midbottom = (randint(900, 1100), self._y_pos))

        self.config()

    @abstractmethod
    def config(self) -> None: 
        pass

    def _animation_state(self) -> None:
        self._animation_index += 0.1

        if self._animation_index >= len(self._frames): self._animation_index = 0
        self.image = self._frames[int(self._animation_index)]

    def _change_obstacle_speed(self, score: int) -> None:
        if score <= 50:
            self.rect.x -= 5
        elif score > 50 and score <= 100:
            self.rect.x -= 10
        elif score > 100 and score <= 200:
            self.rect.x -= 25
        else: 
            self.rect.x -= 30

    def _destroy(self) -> None:
        if self.rect.x <= -100:
            self.kill()

    def update(self, score: int) -> None:
        self._animation_state()
        self._change_obstacle_speed(score=score)
        self._destroy()