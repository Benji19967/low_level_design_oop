from pathlib import Path

import pendulum
from logger import Logger, LogLevel
from output import Console, File

if __name__ == "__main__":
    console = Console()
    file = File(filepath=Path("log_file.txt"))

    logger = Logger(log_level=LogLevel.INFO, output=console)
    logger.log(dt=pendulum.now(), log_level=LogLevel.INFO, message="Info log")
    logger.log(dt=pendulum.now(), log_level=LogLevel.DEBUG, message="Debug log")
    logger.log(dt=pendulum.now(), log_level=LogLevel.WARNING, message="Warning log")

    logger.set_level(log_level=LogLevel.INFO)
    logger.set_output(output=file)
    logger.log(dt=pendulum.now(), log_level=LogLevel.INFO, message="Info log")
    logger.log(dt=pendulum.now(), log_level=LogLevel.DEBUG, message="Debug log")
    logger.log(dt=pendulum.now(), log_level=LogLevel.WARNING, message="Warning log")
