from app.domain.game_state import GameState
from app.domain.level import Level
from app.domain.word import Word


class Application:
    def __init__(self, state: GameState):
        self.state = state

    def init(self, word: Word, level: Level) -> None:
        self.state.set_word(word)
        self.state.set_level(level)

    def validate_letter(self, letter: str) -> None:
        word = self.state.get_word()
        for index, value in enumerate(word.value):
            if value == letter:
                word.mask[index] = True
        self.state.set_word(word)
        self.state.increment_count()

    def validate_word(self) -> tuple[bool, bool]:
        word = self.state.get_word()
        level = self.state.get_level()

        count_limit = -1
        count = self.state.get_count()
        match level:
            case Level.LEVEL_1:
                word.mask[0] = True
                word.mask[-1] = True
            case Level.LEVEL_2:
                count_limit = len(word) * 3
            case Level.LEVEL_3:
                count_limit = len(word) * 2
            case Level.GOD:
                count_limit = len(word)

        win = (False not in word.mask) and (count_limit == -1 or count <= count_limit)
        loose = not win and count_limit != -1 and count > count_limit
        return win, loose
