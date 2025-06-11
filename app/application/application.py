from app.domain.console import Console
from app.domain.level import Level
from app.domain.word_repository import WordRepository


class Application:
    def __init__(self, console: Console, repository: WordRepository):
        self.console = console
        self.repository = repository

    def run(self):
        self.console.welcome()

        word = self.repository.get_random_word()
        level = self.console.get_level()

        finished = False
        count_limit = -1
        count = 1
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

        self.console.interface(word, count_limit)
        while not finished and (count_limit == -1 or count <= count_limit):
            letter_input = self.console.get_letter()

            for index, letter in enumerate(word.value):
                if letter == letter_input:
                    word.mask[index] = True
            self.console.interface(word, count_limit - count)
            count += 1
            if False not in word.mask:
                self.console.win(word.value)
                finished = True
        if count - 1 == count_limit:
            self.console.loose(word.value)
