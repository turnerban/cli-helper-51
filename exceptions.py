from typing import Any

class GameError(Exception):
    """
    Custom exception for general game-related errors.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """
    Exception raised when a player is not found in the game.
    """
    def __init__(self, player_id: str) -> None:
        message = f'Player with ID {player_id} not found.'
        super().__init__(message)
        self.player_id = player_id

class InvalidMoveError(GameError):
    """
    Exception raised for invalid moves in the game.
    """
    def __init__(self, move: Any) -> None:
        message = f'Invalid move attempted: {move}'
        super().__init__(message)
        self.move = move

class GameAlreadyStartedError(GameError):
    """
    Exception raised when trying to start a game that is already running.
    """
    def __init__(self) -> None:
        message = 'Cannot start the game, it is already in progress.'
        super().__init__(message)