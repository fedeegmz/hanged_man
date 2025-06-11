from abc import ABC, abstractmethod

from app.domain.word import Word


class WordRepository(ABC):
    @abstractmethod
    def get_random_word(self) -> Word:
        pass
