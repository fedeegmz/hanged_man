from abc import ABC, abstractmethod

from app.domain.level import Level
from app.domain.word import Word


class GameState(ABC):
    @abstractmethod
    def get_word(self) -> Word | None:
        pass

    @abstractmethod
    def get_level(self) -> Level | None:
        pass

    @abstractmethod
    def get_count(self) -> int:
        pass

    @abstractmethod
    def set_word(self, value: Word) -> None:
        pass

    @abstractmethod
    def set_level(self, value: Level) -> None:
        pass

    @abstractmethod
    def increment_count(self) -> None:
        pass
