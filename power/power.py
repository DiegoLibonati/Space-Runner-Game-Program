import pygame 
from random import randint, choice

class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.power_up_sound = pygame.mixer.Sound("audio/powerup.mp3")
        mistery_frame_1 = pygame.image.load("graphics/PowerCoin/mistery1.png").convert_alpha()
        mistery_frame_2 = pygame.image.load("graphics/PowerCoin/mistery2.png").convert_alpha()
        mistery_frame_3 = pygame.image.load("graphics/PowerCoin/mistery3.png").convert_alpha()
        mistery_frame_4 = pygame.image.load("graphics/PowerCoin/mistery4.png").convert_alpha()
        mistery_frame_5 = pygame.image.load("graphics/PowerCoin/mistery5.png").convert_alpha()
        mistery_frame_6 = pygame.image.load("graphics/PowerCoin/mistery6.png").convert_alpha()
        self.frames = [mistery_frame_1, mistery_frame_2, mistery_frame_3, mistery_frame_4, mistery_frame_5, mistery_frame_6]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]

        y_pos = 300

        self.rect = self.image.get_rect(midbottom = (randint(10, 730), y_pos))
        
        self.score_save = 0
        self.immunity = False

    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self, player):
        self.animation_state()
        self.destroy(player)

    def select_power(self):
        powers = ["immunity"]
        power_selected = choice(powers)

        if power_selected:
            self.immunity = True

    def destroy(self, player):
        if pygame.sprite.collide_rect(player.sprite, self):
            self.power_up_sound.play()
            self.select_power()
            self.kill()

    def power_stop(self, score):
        
        if not self.score_save:
            self.score_save = score

        if self.score_save and self.score_save + 5 == score:
            self.immunity = False
