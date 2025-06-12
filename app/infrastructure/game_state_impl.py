from typing import override

from app.domain.game_state import GameState
from app.domain.level import Level
from app.domain.word import Word


class GameStateImpl(GameState):
    def __init__(self, word: Word | None = None, level: Level | None = None):
        self._word = word
        self._level = level
        self._count = 0

    @override
    def get_word(self) -> Word | None:
        return self._word

    @override
    def get_level(self) -> Level | None:
        return self._level

    @override
    def get_count(self) -> int:
        return self._count

    @override
    def set_word(self, value: Word) -> None:
        self._word = value

    @override
    def set_level(self, value: Level) -> None:
        if self._level is None:
            self._level = value

    @override
    def increment_count(self) -> None:
        self._count += 1
