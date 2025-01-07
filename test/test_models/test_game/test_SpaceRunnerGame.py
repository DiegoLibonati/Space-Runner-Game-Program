from unittest.mock import patch
from unittest.mock import MagicMock

from src.models.power.Power import Power
from src.models.game.SpaceRunnerGame import SpaceRunnerGame

def test_create_space_runner_game(space_runner_game: SpaceRunnerGame) -> None:
    # General
    assert space_runner_game.title == "Space Runner"
    assert space_runner_game.score == 0
    assert space_runner_game.start_time == 0
    assert not space_runner_game._power
    assert not space_runner_game.obstacles_spawn
    assert not space_runner_game.game_started

    # PyGame
    assert space_runner_game.screen
    assert space_runner_game.screen.get_size() == (800, 400)
    assert space_runner_game.clock
    assert space_runner_game.player_single_group
    assert space_runner_game._bg_music
    assert space_runner_game._game_over_music
    assert space_runner_game._obstacle_kill
    assert space_runner_game._primary_font
    assert not space_runner_game.power_single_group
    assert not space_runner_game.obstacle_group

    assert space_runner_game._player_stand_surface
    assert space_runner_game._sky_surface
    assert space_runner_game._game_title_surface
    assert space_runner_game._reset_game_surface
    assert space_runner_game._ground_surface
    assert space_runner_game._player_stand_surface_rect
    assert space_runner_game._game_title_surface_rect
    assert space_runner_game._reset_game_surface_rect

def test_config_game(space_runner_game: SpaceRunnerGame) -> None:
    space_runner_game._config_game()

    assert round(space_runner_game._bg_music.get_volume(), 1) == 0.1
    assert space_runner_game._obstacle_event
    assert space_runner_game._snail_event
    assert space_runner_game._fly_event
    assert space_runner_game._power_event
    assert space_runner_game.player_single_group
    assert space_runner_game.player

def test_create_player(space_runner_game: SpaceRunnerGame) -> None:
    space_runner_game._create_player()

    assert space_runner_game.player_single_group
    assert space_runner_game.player

def test_set_custom_events(space_runner_game: SpaceRunnerGame) -> None:
    space_runner_game._set_custom_events()

    assert space_runner_game._obstacle_event
    assert space_runner_game._snail_event
    assert space_runner_game._fly_event
    assert space_runner_game._power_event

def test_display_score(space_runner_game: SpaceRunnerGame) -> None:
    with patch("pygame.time.get_ticks") as mock_get_ticks:
        mock_get_ticks.return_value = 2000

        score = space_runner_game._display_score()

        assert score
        assert score == 2
        assert isinstance(score, int)

def test_collision_sprite(space_runner_game: SpaceRunnerGame) -> None:
    game_active = space_runner_game._collision_sprite()

    assert game_active

def test_collision_sprite_power_immunity(space_runner_game: SpaceRunnerGame, power: Power) -> None:
    power.current_power = "immunity"
    power.stop_power = MagicMock()

    space_runner_game._power = power
    game_active = space_runner_game._collision_sprite()

    assert game_active
    power.stop_power.assert_called_once()
    
def test_collision_sprite_power_killer(space_runner_game: SpaceRunnerGame, power: Power) -> None:
    power.current_power = "killer"
    power.stop_power = MagicMock()

    space_runner_game._power = power
    game_active = space_runner_game._collision_sprite()

    assert game_active
    power.stop_power.assert_called_once()

def test_collision_sprite_lose(space_runner_game: SpaceRunnerGame) -> None:
    with patch("pygame.sprite.spritecollide") as mock_get_ticks:
        mock_get_ticks.return_value = True

        space_runner_game.obstacle_group.empty = MagicMock()
        space_runner_game.power_single_group.empty = MagicMock()

        game_active = space_runner_game._collision_sprite()

        assert not game_active
        space_runner_game.obstacle_group.empty.assert_called_once()
        space_runner_game.power_single_group.empty.assert_called_once()