from src.models.game.SpaceRunnerGame import SpaceRunnerGame


def main() -> None:
    game = SpaceRunnerGame()
    game.game_loop()


if __name__ == "__main__":
    main()