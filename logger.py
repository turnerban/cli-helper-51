import logging
from typing import Optional

class Logger:
    """
    Custom logger for game events and errors.
    """

    def __init__(self, name: str, level: Optional[int] = logging.INFO) -> None:
        """
        Initializes the Logger with the specified name and log level.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message: str) -> None:
        """
        Logs an informational message.
        """
        self.logger.info(message)

    def log_warning(self, message: str) -> None:
        """
        Logs a warning message.
        """
        self.logger.warning(message)

    def log_error(self, message: str) -> None:
        """
        Logs an error message.
        """
        self.logger.error(message)

    def log_debug(self, message: str) -> None:
        """
        Logs a debug message.
        """
        self.logger.debug(message)

# Example usage:
if __name__ == '__main__':
    game_logger = Logger('GameLogger')
    game_logger.log_info('Game has started.')
    game_logger.log_warning('Low health warning.')
    game_logger.log_error('An error occurred.')
    game_logger.log_debug('Debugging the game state.')