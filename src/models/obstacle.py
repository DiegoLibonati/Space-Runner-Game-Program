import pygame 
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(
        self, type: str = "", frames: list = [],
        y_pos: int = 0, animation_index: int = 0, image: pygame.image = None,
        rect: pygame.Rect = None
    ):
        super().__init__()

        self.frames = frames
        self.type = type
        self.y_pos = y_pos
        self.animation_index = animation_index
        self.image = image
        self.rect = rect


    def animation_state(
        self
    ) -> None:
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def update(
        self, score: int
    ) -> None:
        self.animation_state()
        if score <= 50:
            self.rect.x -= 5
        elif score > 50 and score <= 100:
            self.rect.x -= 10
        elif score > 100 and score <= 200:
            self.rect.x -= 25
        else: 
            self.rect.x -= 30

        self.destroy()


    def init_obstacle(self) -> None:
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), self.y_pos))


    def destroy(
        self
    ) -> None:
        if self.rect.x <= -100:
            self.kill()
