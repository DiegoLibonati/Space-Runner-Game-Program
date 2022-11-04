import pygame 
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
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

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self, score):
        self.animation_state()
        if score <= 50:
            self.rect.x -= 5
        elif score > 50 and score <= 100:
            self.rect.x -= 10
        else: 
            self.rect.x -= 10

        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
