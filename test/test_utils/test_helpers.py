from src.models.obstacles import Bat, Grounder, Snail
from src.utils.helpers import get_obstacle_by_type


def test_invalid_obstacle() -> None:
    assert not get_obstacle_by_type(type="invalid")


def test_obstacle_snail() -> None:
    snail = get_obstacle_by_type(type="snail")

    assert isinstance(snail, Snail)
    assert snail._frames
    assert snail._y_pos == 300


def test_obstacle_bat() -> None:
    bat = get_obstacle_by_type(type="bat")

    assert isinstance(bat, Bat)
    assert bat._frames
    assert bat._y_pos == 210


def test_obstacle_grounder() -> None:
    grounder = get_obstacle_by_type(type="grounder")

    assert isinstance(grounder, Grounder)
    assert grounder._frames
    assert grounder._y_pos == 300
