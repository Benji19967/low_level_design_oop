from datetime import datetime
from threading import Lock

from log_level import LogLevel
from output import Console, Output


class Logger:

    _instance = None

    def __init__(
        self, log_level: LogLevel = LogLevel.INFO, output: Output = Console()
    ) -> None:
        if Logger._instance is not None:
            raise Exception("Logger already exists, this class is a singleton!")
        Logger._instance = self

        self._log_level = log_level
        self._output = output
        self._lock = Lock()

    @staticmethod
    def get_instance() -> "Logger":
        if Logger._instance is None:
            Logger()
        assert Logger._instance
        return Logger._instance

    def log(self, dt: datetime, log_level: LogLevel, message: str) -> None:
        if log_level >= self._log_level:
            with self._lock:
                self._output.write(dt=dt, log_level=log_level, message=message)

    def set_level(self, log_level: LogLevel) -> None:
        self._log_level = log_level

    def set_output(self, output: Output) -> None:
        self._output = output
