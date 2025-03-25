from pathlib import Path

from log_level import LogLevel
from logger import Logger
from output import Console, File

if __name__ == "__main__":
    console = Console()
    file = File(filepath=Path("log_file.txt"))

    logger = Logger(log_level=LogLevel.INFO, output=console)
    logger.info(message="Info log")
    logger.debug(message="Debug log")
    logger.warning(message="Warning log")

    logger.set_level(log_level=LogLevel.WARNING)
    logger.set_output(output=file)
    logger.info(message="Info log")
    logger.debug(message="Debug log")
    logger.warning(message="Warning log")
