from random import randint

from app.domain.word import Word


class WordRepository:
    def __init__(self):
        self.words: list[str] = []
        self._load_data()

    def get_random_word(self) -> Word:
        num = randint(0, len(self.words))
        return Word(value=self.words[num])

    def _load_data(self) -> None:
        with open("data/words.txt", "r", encoding="utf-8") as f:
            for line in f:
                self.words.append(line.replace("\n", ""))
