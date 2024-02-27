import pygame 
from random import randint, choice

class Power(pygame.sprite.Sprite):
    def __init__(
        self, frames: list = [], power_sound: pygame.mixer = None,
        animation_index: int = 0, image: pygame.image = None, y_pos: int = 300,
        rect: pygame.Rect = None, score_save: int = 0, immunity: bool = False,
        killer: bool = False
    ):
        super().__init__()

        self.power_up_sound = power_sound
        self.frames = frames

        self.animation_index = animation_index
        self.image = image

        self.y_pos = y_pos

        self.rect = rect
        
        self.score_save = score_save
        self.immunity = immunity
        self.killer = killer


    def init_power(
        self
    ) -> None:
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(10, 730), self.y_pos))


    def animation_state(
        self
    ) -> None:
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def update(
        self, player: pygame.sprite.GroupSingle
    ) -> None:
        self.animation_state()
        self.destroy(player)


    def select_power(
        self
    ) -> None:
        powers = ["immunity", "killer"]
        power_selected = choice(powers)
        if power_selected == "immunity":
            self.immunity = True
        elif power_selected == "killer":
            self.killer = True


    def destroy(
        self, player: pygame.sprite.GroupSingle
    ) -> None:
        if pygame.sprite.collide_rect(player.sprite, self):
            self.power_up_sound.play()
            self.select_power()
            self.kill()


    def power_stop(
        self, score: int
    ) -> None:
        
        if not self.score_save:
            self.score_save = score

        if self.score_save and self.score_save + 5 == score:
            self.immunity = False
            self.killer = False
