from unittest.mock import MagicMock, patch

from src.models.power import Power


def test_create_power(power: Power) -> None:
    assert power
    assert power._animation_index == 0
    assert power._y_pos == 300
    assert power._frames
    assert power._power_pick_sound
    assert power.image
    assert power.rect
    assert not power._power_reset_time
    assert not power.current_power


def test_config_power(power: Power) -> None:
    power._config()
    pass


def test_animation_state(power: Power) -> None:
    assert power._animation_index == 0

    power._animation_state()

    assert power._animation_index == 0.1
    assert power.image == power._frames[int(power._animation_index)]

    power._animation_index = 0.9

    power._animation_state()

    assert power._animation_index == 1
    assert power.image == power._frames[int(power._animation_index)]


def test_select_power(power: Power) -> None:
    assert not power.current_power

    power._select_power()

    assert power.current_power


def test_pick_up(power: Power) -> None:
    player = MagicMock()
    player.sprite = MagicMock()

    with patch("pygame.sprite.collide_rect") as mock_collide_rect:
        mock_collide_rect.return_value = True

        power._pick_up(player=player)

        assert power.current_power


def test_stop_power(power: Power) -> None:
    with patch("pygame.time.get_ticks") as mock_get_ticks:
        mock_get_ticks.return_value = 1000

        assert not power.current_power

        power._select_power()
        assert power.current_power

        mock_get_ticks.return_value = 7000
        power.stop_power()

        assert not power.current_power
