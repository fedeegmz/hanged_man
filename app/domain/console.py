from abc import ABC, abstractmethod

from app.domain.level import Level
from app.domain.word import Word


class Console(ABC):
    @abstractmethod
    def welcome(self) -> None:
        pass

    @abstractmethod
    def interface(self, word: Word, count: int = 0) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_level() -> Level:
        pass

    @staticmethod
    @abstractmethod
    def get_letter() -> str:
        pass

    @staticmethod
    @abstractmethod
    def win(word: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def loose(word: str) -> None:
        pass
