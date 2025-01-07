import pytest

import pygame

from src.models.power.Power import Power
from src.models.player.Player import Player
from src.models.obstacles.bat.Bat import Bat
from src.models.obstacles.snail.Snail import Snail
from src.models.obstacles.grounder.Grounder import Grounder
from src.models.game.SpaceRunnerGame import SpaceRunnerGame
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