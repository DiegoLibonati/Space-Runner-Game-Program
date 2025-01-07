from unittest.mock import MagicMock

from src.models.obstacles.bat.Bat import Bat


def test_create_bat(bat: Bat) -> None:
    assert bat
    assert bat._frames
    assert bat._y_pos == 210
    assert bat._animation_index == 0
    assert bat.image
    assert bat.rect

def test_config_bat(bat: Bat) -> None:
    bat.config()
    pass

def test_animation_state(bat: Bat) -> None:
    assert bat._animation_index == 0

    bat._animation_state()

    assert bat._animation_index == 0.1
    assert bat.image == bat._frames[int(bat._animation_index)]

    bat._animation_index = 0.9

    bat._animation_state()

    assert bat._animation_index == 1
    assert bat.image == bat._frames[int(bat._animation_index)]

def test_change_obstacle_speed(bat: Bat) -> None:
    prev_rect_x = bat.rect.x

    bat._change_obstacle_speed(score=40)

    assert bat.rect.x == prev_rect_x - 5

    prev_rect_x = bat.rect.x

    bat._change_obstacle_speed(score=60)

    assert bat.rect.x == prev_rect_x - 10

    prev_rect_x = bat.rect.x

    bat._change_obstacle_speed(score=120)

    assert bat.rect.x == prev_rect_x - 25

    prev_rect_x = bat.rect.x

    bat._change_obstacle_speed(score=2003)

    assert bat.rect.x == prev_rect_x - 30

def test_destroy(bat: Bat) -> None:
    bat.kill = MagicMock()

    bat.rect.x = -90
    bat._destroy()
    bat.kill.assert_not_called()

    bat.rect.x = -120
    bat._destroy()
    bat.kill.assert_called_once()