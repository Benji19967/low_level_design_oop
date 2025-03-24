from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5

    def __ge__(self, other: "LogLevel") -> bool:
        if self.__class__ == other.__class__:
            return self.value >= other.value
        return NotImplemented
