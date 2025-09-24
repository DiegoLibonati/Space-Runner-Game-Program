import math
from random import choice, randint
from sys import exit

import pygame

from src.core.paths import (
    BG_GAME_SOUND,
    GAME_OVER_GAME_SOUND,
    GROUND,
    OBSTACLE_KILL_SOUND,
    PLAYER_STAND_1,
    PRIMARY_FONT,
    SKY,
)
from src.models.player import Player
from src.models.power import Power
from src.utils.helpers import get_obstacle_by_type


class SpaceRunnerGame:
    def __init__(self) -> None:
        pygame.init()

        self._title: str = "Space Runner"
        self._game_started: bool = False
        self._score: int = 0
        self._start_time: int = 0
        self._obstacles_spawn: list[str] = []
        self._power: Power = None

        pygame.display.set_caption(self.title)
        self._screen = pygame.display.set_mode(((800, 400)))
        self._clock = pygame.time.Clock()
        self._player_single_group = pygame.sprite.GroupSingle()
        self._power_single_group = pygame.sprite.GroupSingle()
        self._obstacle_group = pygame.sprite.Group()
        self._bg_music: pygame.mixer.Sound = pygame.mixer.Sound(BG_GAME_SOUND)
        self._game_over_music: pygame.mixer.Sound = pygame.mixer.Sound(
            GAME_OVER_GAME_SOUND
        )
        self._obstacle_kill: pygame.mixer.Sound = pygame.mixer.Sound(
            OBSTACLE_KILL_SOUND
        )
        self._primary_font = pygame.font.Font(PRIMARY_FONT, 50)

        self._player_stand_surface = pygame.transform.scale2x(
            pygame.image.load(PLAYER_STAND_1).convert_alpha()
        )
        self._sky_surface = pygame.image.load(SKY).convert()
        self._game_title_surface = self._primary_font.render(
            self.title, False, (111, 196, 169)
        )
        self._reset_game_surface = self._primary_font.render(
            "Reset game with SPACE", False, (111, 196, 169)
        )
        self._ground_surface = pygame.image.load(GROUND).convert()
        self._player_stand_surface_rect = self._player_stand_surface.get_rect(
            center=(400, 200)
        )
        self._game_title_surface_rect = self._game_title_surface.get_rect(
            center=(400, 50)
        )
        self._reset_game_surface_rect = self._reset_game_surface.get_rect(
            center=(400, 350)
        )

        self._config_game()

    @property
    def title(self) -> str:
        return self._title

    @property
    def screen(self) -> pygame.Surface:
        return self._screen

    @property
    def game_started(self) -> bool:
        return self._game_started

    @property
    def score(self) -> int:
        return self._score

    @property
    def start_time(self) -> int:
        return self._start_time

    @property
    def obstacles_spawn(self) -> list[str]:
        return self._obstacles_spawn

    @property
    def player_single_group(self) -> pygame.sprite.GroupSingle:
        return self._player_single_group

    @property
    def player(self) -> Player:
        return self.player_single_group.sprites()[0]

    @property
    def power_single_group(self) -> pygame.sprite.GroupSingle:
        return self._power_single_group

    @property
    def power(self) -> Power:
        return self._power

    @property
    def obstacle_group(self) -> pygame.sprite.Group:
        return self._obstacle_group

    @property
    def clock(self) -> pygame.time.Clock:
        return self._clock

    def _config_game(self) -> None:
        self._bg_music.set_volume(0.1)
        self._set_custom_events()
        self._create_player()

    def _create_player(self) -> None:
        player = Player()
        self.player_single_group.add(player)

    def _set_custom_events(self) -> None:
        self._obstacle_event = pygame.USEREVENT + 10
        pygame.time.set_timer(self._obstacle_event, 1500)

        self._snail_event = pygame.USEREVENT + 11
        pygame.time.set_timer(self._snail_event, 500)

        self._fly_event = pygame.USEREVENT + 12
        pygame.time.set_timer(self._fly_event, 500)

        self._power_event = pygame.USEREVENT + 13
        pygame.time.set_timer(self._power_event, randint(15000, 30000))

    def _display_score(self) -> int:
        current_time = pygame.time.get_ticks() - self.start_time
        current_time = math.floor(current_time / 1000)

        score_surface = self._primary_font.render(
            f"Score: {current_time}", False, (64, 64, 64)
        )
        score_surface_rect = score_surface.get_rect(center=(400, 50))

        self.screen.blit(score_surface, score_surface_rect)

        return current_time

    def _collision_sprite(self) -> bool:
        if self.power and self.power.current_power == "immunity":
            self.power.stop_power()

            return True

        if self.power and self.power.current_power == "killer":
            self.power.stop_power()

            if pygame.sprite.spritecollide(
                self.player_single_group.sprite, self.obstacle_group, False
            ):
                for obstacle in self.obstacle_group:
                    if pygame.sprite.collide_rect(
                        self.player_single_group.sprite, obstacle
                    ):
                        self._obstacle_kill.play()
                        obstacle.kill()

                        return True

        if pygame.sprite.spritecollide(
            self.player_single_group.sprite, self.obstacle_group, False
        ):
            self.obstacle_group.empty()
            self.power_single_group.empty()

            self._game_over_music.play()
            self._bg_music.stop()

            return False

        return True

    def game_loop(self) -> None:
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if (
                    not self.game_started
                    and event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                ):
                    self._game_started = True
                    self._start_time = pygame.time.get_ticks()

                    self._bg_music.play(loops=-1)
                    self._game_over_music.stop()

                if (
                    self.game_started
                    and event.type == self._obstacle_event
                    and self.score >= 0
                    and "snail" not in self.obstacles_spawn
                ):
                    self._obstacles_spawn.append("snail")

                if (
                    self.game_started
                    and event.type == self._obstacle_event
                    and self.score >= 10
                    and "bat" not in self.obstacles_spawn
                ):
                    self._obstacles_spawn.append("bat")

                if (
                    self.game_started
                    and event.type == self._obstacle_event
                    and self.score >= 20
                    and "grounder" not in self.obstacles_spawn
                ):
                    self._obstacles_spawn.append("grounder")

                if self.game_started and event.type == self._obstacle_event:
                    obstacle = get_obstacle_by_type(type=choice(self.obstacles_spawn))
                    self.obstacle_group.add(obstacle)

                if self.game_started and event.type == self._power_event:
                    self._power = Power()
                    self.power_single_group.add(self.power)

            if not self.game_started:
                self.screen.fill((94, 129, 162))
                self.screen.blit(
                    self._player_stand_surface, self._player_stand_surface_rect
                )
                self.screen.blit(
                    self._game_title_surface, self._game_title_surface_rect
                )
                self.screen.blit(
                    self._reset_game_surface, self._reset_game_surface_rect
                )

            if not self.game_started and self.score:
                final_score_surface = self._primary_font.render(
                    f"Score: {self.score}", False, (111, 196, 169)
                )
                final_score_surface_rect = final_score_surface.get_rect(
                    center=(400, 80)
                )

                self.screen.blit(final_score_surface, final_score_surface_rect)

            if self.game_started:
                self.screen.blit(self._sky_surface, (0, 0))
                self.screen.blit(self._ground_surface, (0, 300))

                self._score = self._display_score()

                # Draw
                self.player_single_group.draw(surface=self.screen)
                self.player_single_group.update()

                if self.power:
                    self.player.change_skin_player(power=self.power.current_power)

                self.obstacle_group.draw(surface=self.screen)
                self.obstacle_group.update(score=self.score)

                self.power_single_group.draw(surface=self.screen)
                self.power_single_group.update(player=self.player_single_group)

                # Si sigue activo
                self._game_started = self._collision_sprite()

            pygame.display.update()
            # Frames. 60 FPS
            self.clock.tick(60)
