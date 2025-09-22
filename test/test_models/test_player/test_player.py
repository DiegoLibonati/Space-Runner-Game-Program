from unittest.mock import patch
from unittest.mock import MagicMock

import pygame

from src.models import Player

def test_create_player(player: Player) -> None:
    assert player
    assert player._walk_index == 0
    assert player._gravity == 0
    assert player._walk_frames
    assert player._jump_frame
    assert player._jump_sound
    assert player.image
    assert player.rect
    assert not player.is_jump

def test_config_player(player: Player) -> None:
    player._config()
    
    assert round(player._jump_sound.get_volume(), 1) == 0.2

def test_input_jump(player: Player) -> None:
    mock_keys = [0] * 323
    mock_keys[pygame.K_SPACE] = 1

    with patch("pygame.key.get_pressed", return_value=mock_keys):
        player._jump_sound = MagicMock()

        player._input()

        assert player._gravity == -20
        player._jump_sound.play.assert_called_once()

def test_input_d(player: Player) -> None:
    prev_rect_x = player.rect.x
    mock_keys = [0] * 323
    mock_keys[pygame.K_d] = 1

    with patch("pygame.key.get_pressed", return_value=mock_keys):
        player._input()

        assert player.rect.x == prev_rect_x + 2

def test_input_a(player: Player) -> None:
    prev_rect_x = player.rect.x
    mock_keys = [0] * 323
    mock_keys[pygame.K_a] = 1

    with patch("pygame.key.get_pressed", return_value=mock_keys):
        player._input()

        assert player.rect.x == prev_rect_x - 2

def test_apply_gravity(player: Player) -> None:
    prev_rect_y = player.rect.y
    player._gravity = -20

    player._apply_gravity()

    current_gravity = -19

    assert player._gravity == current_gravity
    assert player.rect.y == prev_rect_y + current_gravity
    assert player.rect.bottom != 300
    assert player.is_jump

def test_animation_state_jump(player: Player) -> None:
    player.rect.bottom = 299

    player._animation_state()

    assert player.is_jump
    assert player.image == player._jump_frame
    
def test_animation_state_not_jump(player: Player) -> None:
    player._animation_state()

    assert not player.is_jump
    assert player.image != player._jump_frame
    assert player.image == player._walk_frames[0]

def test_animation_state_walk(player: Player) -> None:
    mock_keys = [0] * 323
    mock_keys[pygame.K_a] = 1

    with patch("pygame.key.get_pressed", return_value=mock_keys):
        player._animation_state()

        assert not player.is_jump
        assert player.image != player._jump_frame
        assert player._walk_index == 0.1
        assert player.image == player._walk_frames[int(player._walk_index)]

        player._walk_index = 0.9

        player._animation_state()

        assert player._walk_index == 1
        assert player._walk_frames[int(player._walk_index)]

def test_limits(player: Player) -> None:
    player.rect.x = -2

    player._limits()

    assert player.rect.x == 0

    player.rect.x = 1000

    player._limits()

    assert player.rect.x == 735

def test_change_skin_player(player: Player) -> None:
    prev_frames = player._walk_frames
    prev_jump_frame = player._jump_frame

    player.change_skin_player(power="immunity")

    assert player._walk_frames != prev_frames
    assert player._jump_frame != prev_jump_frame

    prev_frames = player._walk_frames
    prev_jump_frame = player._jump_frame

    player.change_skin_player(power="killer")

    assert player._walk_frames != prev_frames
    assert player._jump_frame != prev_jump_frame

    prev_frames = player._walk_frames
    prev_jump_frame = player._jump_frame

    player.change_skin_player(power="")

    assert player._walk_frames != prev_frames
    assert player._jump_frame != prev_jump_frame

    prev_frames = player._walk_frames
    prev_jump_frame = player._jump_frame