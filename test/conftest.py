import pytest

import pygame

from src.models import Power, Player, Bat, Snail, Grounder, SpaceRunnerGame
from src.utils.utils import get_obstacle_by_type

def pytest_sessionstart() -> None:
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    pygame.init()
    pygame.display.set_mode(((800, 400)))
    

def pytest_sessionfinish() -> None:
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    pygame.quit()


@pytest.fixture
def space_runner_game() -> SpaceRunnerGame:
    return SpaceRunnerGame()


@pytest.fixture
def power() -> Power:
    return Power()


@pytest.fixture
def player() -> Player:
    return Player()


@pytest.fixture
def bat() -> Bat:
    return get_obstacle_by_type(type="bat")


@pytest.fixture
def snail() -> Snail:
    return get_obstacle_by_type(type="snail")


@pytest.fixture
def grounder() -> Grounder:
    return get_obstacle_by_type(type="grounder")