from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from pathlib import Path

import pendulum
from log_level import LogLevel


class OutputDestination(Enum):
    CONSOLE = 1
    FILE = 2
    DATABASE = 3


class Output(ABC):
    @abstractmethod
    def write(
        self,
        log_level: LogLevel,
        message: str,
    ) -> None:
        raise NotImplementedError


class Console(Output):
    def write(
        self,
        log_level: LogLevel,
        message: str,
    ) -> None:
        print(f"{pendulum.now()} - {str(log_level.name)}: {message}")


class File(Output):
    def __init__(self, filepath: Path) -> None:
        super().__init__()
        self._filepath = filepath

    def write(
        self,
        log_level: LogLevel,
        message: str,
    ) -> None:
        with open(self._filepath, "a") as f:
            f.write(f"{pendulum.now()} - {str(log_level.name)}: {message}\n")
