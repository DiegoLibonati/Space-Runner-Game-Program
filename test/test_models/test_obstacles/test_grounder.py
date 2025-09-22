from unittest.mock import MagicMock

from src.models import Grounder


def test_create_grounder(grounder: Grounder) -> None:
    assert grounder
    assert grounder._frames
    assert grounder._y_pos == 300
    assert grounder._animation_index == 0
    assert grounder.image
    assert grounder.rect

def test_config_grounder(grounder: Grounder) -> None:
    grounder.config()
    pass

def test_animation_state(grounder: Grounder) -> None:
    assert grounder._animation_index == 0

    grounder._animation_state()

    assert grounder._animation_index == 0.1
    assert grounder.image == grounder._frames[int(grounder._animation_index)]

    grounder._animation_index = 0.9

    grounder._animation_state()

    assert grounder._animation_index == 1
    assert grounder.image == grounder._frames[int(grounder._animation_index)]

def test_change_obstacle_speed(grounder: Grounder) -> None:
    prev_rect_x = grounder.rect.x

    grounder._change_obstacle_speed(score=40)

    assert grounder.rect.x == prev_rect_x - 5

    prev_rect_x = grounder.rect.x

    grounder._change_obstacle_speed(score=60)

    assert grounder.rect.x == prev_rect_x - 10

    prev_rect_x = grounder.rect.x

    grounder._change_obstacle_speed(score=120)

    assert grounder.rect.x == prev_rect_x - 25

    prev_rect_x = grounder.rect.x

    grounder._change_obstacle_speed(score=2003)

    assert grounder.rect.x == prev_rect_x - 30

def test_destroy(grounder: Grounder) -> None:
    grounder.kill = MagicMock()

    grounder.rect.x = -90
    grounder._destroy()
    grounder.kill.assert_not_called()

    grounder.rect.x = -120
    grounder._destroy()
    grounder.kill.assert_called_once()