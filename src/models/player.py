import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(
        self, player_walk_frames: list = [], player_jump: pygame.image = None,
        image: pygame.image = None, player_index: int = 0, is_jump: bool = False,
        rect: pygame.Rect = None, gravity: int = 0, jump_sound: pygame.mixer = None
    ):
        super().__init__()

        self.player_jump = player_jump
        self.player_walk_frames = player_walk_frames

        self.player_index = player_index
        self.is_jump = is_jump

        self.image = image
        self.rect = rect
        self.gravity = gravity

        self.jump_sound = jump_sound
    
    def init_player(
        self
    ) -> None:

        self.image = self.player_walk_frames[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.jump_sound.set_volume(0.2)
        pass


    def player_input(
        self
    ) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20
        if keys[pygame.K_d]:
            self.rect.x += 2
        if keys[pygame.K_a]:
            self.rect.x += -2


    def apply_gravity(
        self
    ) -> None:
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300


    def animation_state(
        self
    ) -> None:

        if self.rect.bottom < 300 and not self.is_jump:
            self.image = self.player_jump
            self.is_jump = True
        else:
            keys = pygame.key.get_pressed()
            
            if self.is_jump and self.rect.bottom == 300:
                self.is_jump = False
                self.image = self.player_walk_frames[0]

            if (keys[pygame.K_d] or keys[pygame.K_a]) and self.rect.bottom == 300: 
                self.player_index += 0.1
                if self.player_index >= len(self.player_walk_frames): self.player_index = 0
                self.image = self.player_walk_frames[int(self.player_index)]


    def limit_map(
        self
    ) -> None:
        if self.rect.x <= 0:
            self.rect.x = 1
        if self.rect.x >= 736:
            self.rect.x = 735


    def change_skin_player(
        self, power: dict
    ) -> None:
        
        if power.immunity and not power.killer:
            self.player_walk_1 = pygame.image.load("./src/graphics/player/player_walk_1_immunity.png").convert_alpha()
            self.player_walk_2 = pygame.image.load("./src/graphics/player/player_walk_2_immunity.png").convert_alpha()
            self.player_jump = pygame.image.load("./src/graphics/player/jump_immunity.png").convert_alpha()
            self.player_walk_frames = [self.player_walk_1, self.player_walk_2]
        elif power.killer and not power.immunity:
            self.player_walk_1 = pygame.image.load("./src/graphics/player/player_walk_1_killer.png").convert_alpha()
            self.player_walk_2 = pygame.image.load("./src/graphics/player/player_walk_2_killer.png").convert_alpha()
            self.player_jump = pygame.image.load("./src/graphics/player/jump_killer.png").convert_alpha()
            self.player_walk_frames = [self.player_walk_1, self.player_walk_2]
        else:
            self.player_walk_1 = pygame.image.load("./src/graphics/player/player_walk_1.png").convert_alpha()
            self.player_walk_2 = pygame.image.load("./src/graphics/player/player_walk_2.png").convert_alpha()
            self.player_jump = pygame.image.load("./src/graphics/player/jump.png").convert_alpha()
            self.player_walk_frames = [self.player_walk_1, self.player_walk_2]


    def update(
        self
    ) -> None:
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        self.limit_map()
        