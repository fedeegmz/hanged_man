from app.application.application import Application
from app.domain.game_state import GameState
from app.infrastructure.console import Console
from app.infrastructure.game_state_impl import GameStateImpl
from app.infrastructure.word_repository import WordRepository


class Game:
    console = Console()
    word_repository = WordRepository()
    game_state: GameState = GameStateImpl()
    application = Application(game_state)

    def run(self) -> None:
        self.console.welcome()
        word = self.word_repository.get_random_word()
        level = self.console.get_level()
        self.application.init(word, level)
        win, loose = self.application.validate_word()
        while not win and not loose:
            self.console.interface(word, count=self.game_state.get_count())
            letter = self.console.get_letter()
            self.application.validate_letter(letter)
            win, loose = self.application.validate_word()
        if win:
            self.console.win(word.value)
        elif loose:
            self.console.loose(word.value)
