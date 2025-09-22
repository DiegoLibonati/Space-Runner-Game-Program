import pygame

from src.constants.paths import (
    PLAYER_IMMUNITY_JUMP_1,
    PLAYER_IMMUNITY_WALK_1,
    PLAYER_IMMUNITY_WALK_2,
    PLAYER_JUMP_1,
    PLAYER_JUMP_SOUND_1,
    PLAYER_KILLER_JUMP_1,
    PLAYER_KILLER_WALK_1,
    PLAYER_KILLER_WALK_2,
    PLAYER_WALK_1,
    PLAYER_WALK_2,
)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self._walk_index: int = 0
        self._gravity: int = 0

        self._walk_frames: list[pygame.Surface] = [
            pygame.image.load(PLAYER_WALK_1).convert_alpha(),
            pygame.image.load(PLAYER_WALK_2).convert_alpha(),
        ]
        self._jump_frame: pygame.Surface = pygame.image.load(
            PLAYER_JUMP_1
        ).convert_alpha()
        self._jump_sound: pygame.mixer.Sound = pygame.mixer.Sound(PLAYER_JUMP_SOUND_1)

        self.image: pygame.Surface = self._walk_frames[self._walk_index]
        self.rect: pygame.Rect = self.image.get_rect(midbottom=(80, 300))

        self._config()

    @property
    def is_jump(self) -> bool:
        return self.rect.bottom < 300

    def _config(self) -> None:
        self._jump_sound.set_volume(0.2)

    def _input(self) -> None:
        keys = pygame.key.get_pressed()

        space = keys[pygame.K_SPACE]
        a = keys[pygame.K_a]
        d = keys[pygame.K_d]

        if space and self.rect.bottom >= 300:
            self._jump_sound.play()
            self._gravity = -20
        elif d:
            self.rect.x += 2
        elif a:
            self.rect.x -= 2

    def _apply_gravity(self) -> None:
        self._gravity += 1
        self.rect.y += self._gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def _animation_state(self) -> None:
        if self.is_jump:
            self.image = self._jump_frame
            return

        keys = pygame.key.get_pressed()

        a = keys[pygame.K_a]
        d = keys[pygame.K_d]

        if not self.is_jump:
            self.image = self._walk_frames[0]

        if (a or d) and not self.is_jump:
            self._walk_index += 0.1
            if self._walk_index >= len(self._walk_frames):
                self._walk_index = 0
            self.image = self._walk_frames[int(self._walk_index)]

    def _limits(self) -> None:
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= 735:
            self.rect.x = 735

    def change_skin_player(self, power: str) -> None:
        if power == "immunity":
            self._walk_frames = [
                pygame.image.load(PLAYER_IMMUNITY_WALK_1).convert_alpha(),
                pygame.image.load(PLAYER_IMMUNITY_WALK_2).convert_alpha(),
            ]
            self._jump_frame = pygame.image.load(PLAYER_IMMUNITY_JUMP_1).convert_alpha()
        elif power == "killer":
            self._walk_frames = [
                pygame.image.load(PLAYER_KILLER_WALK_1).convert_alpha(),
                pygame.image.load(PLAYER_KILLER_WALK_2).convert_alpha(),
            ]
            self._jump_frame = pygame.image.load(PLAYER_KILLER_JUMP_1).convert_alpha()
        else:
            self._walk_frames = [
                pygame.image.load(PLAYER_WALK_1).convert_alpha(),
                pygame.image.load(PLAYER_WALK_2).convert_alpha(),
            ]
            self._jump_frame = pygame.image.load(PLAYER_JUMP_1).convert_alpha()

    def update(self) -> None:
        self._input()
        self._apply_gravity()
        self._animation_state()
        self._limits()
