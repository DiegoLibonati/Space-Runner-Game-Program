from random import choice, randint

import pygame

from src.core.paths import (
    POWER_MISTERY_ANIMATION_1,
    POWER_MISTERY_ANIMATION_2,
    POWER_MISTERY_ANIMATION_3,
    POWER_MISTERY_ANIMATION_4,
    POWER_MISTERY_ANIMATION_5,
    POWER_MISTERY_ANIMATION_6,
    POWER_MISTERY_ANIMATION_7,
    POWER_PICK_SOUND_1,
)


class Power(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self._animation_index = 0
        self._y_pos = 300
        self._power_reset_time: int = None
        self.current_power: str = ""

        self._frames: list[pygame.Surface] = [
            pygame.image.load(POWER_MISTERY_ANIMATION_1).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_2).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_3).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_4).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_5).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_6).convert_alpha(),
            pygame.image.load(POWER_MISTERY_ANIMATION_7).convert_alpha(),
        ]
        self._power_pick_sound: pygame.mixer.Sound = pygame.mixer.Sound(
            POWER_PICK_SOUND_1
        )

        self.image: pygame.Surface = self._frames[self._animation_index]
        self.rect: pygame.Rect = self.image.get_rect(
            midbottom=(randint(10, 730), self._y_pos)
        )

        self._config()

    def _config(self) -> None:
        pass

    def _animation_state(self) -> None:
        self._animation_index += 0.1

        if self._animation_index >= len(self._frames):
            self._animation_index = 0
        self.image = self._frames[int(self._animation_index)]

    def update(self, player: pygame.sprite.GroupSingle) -> None:
        self._animation_state()
        self._pick_up(player=player)

    def _select_power(self) -> None:
        powers = ["immunity", "killer"]
        self.current_power = choice(powers)
        self._power_reset_time = pygame.time.get_ticks() + 5000

    def _pick_up(self, player: pygame.sprite.GroupSingle) -> None:
        if not pygame.sprite.collide_rect(player.sprite, self):
            return

        self._power_pick_sound.play()
        self._select_power()
        self.kill()

    def stop_power(self) -> None:
        if self.current_power and pygame.time.get_ticks() >= self._power_reset_time:
            self.current_power = ""
