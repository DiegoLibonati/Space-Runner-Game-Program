from unittest.mock import MagicMock

from src.models import Snail


def test_create_snail(snail: Snail) -> None:
    assert snail
    assert snail._frames
    assert snail._y_pos == 300
    assert snail._animation_index == 0
    assert snail.image
    assert snail.rect

def test_config_snail(snail: Snail) -> None:
    snail.config()
    pass

def test_animation_state(snail: Snail) -> None:
    assert snail._animation_index == 0

    snail._animation_state()

    assert snail._animation_index == 0.1
    assert snail.image == snail._frames[int(snail._animation_index)]

    snail._animation_index = 0.9

    snail._animation_state()

    assert snail._animation_index == 1
    assert snail.image == snail._frames[int(snail._animation_index)]

def test_change_obstacle_speed(snail: Snail) -> None:
    prev_rect_x = snail.rect.x

    snail._change_obstacle_speed(score=40)

    assert snail.rect.x == prev_rect_x - 5

    prev_rect_x = snail.rect.x

    snail._change_obstacle_speed(score=60)

    assert snail.rect.x == prev_rect_x - 10

    prev_rect_x = snail.rect.x

    snail._change_obstacle_speed(score=120)

    assert snail.rect.x == prev_rect_x - 25

    prev_rect_x = snail.rect.x

    snail._change_obstacle_speed(score=2003)

    assert snail.rect.x == prev_rect_x - 30

def test_destroy(snail: Snail) -> None:
    snail.kill = MagicMock()

    snail.rect.x = -90
    snail._destroy()
    snail.kill.assert_not_called()

    snail.rect.x = -120
    snail._destroy()
    snail.kill.assert_called_once()