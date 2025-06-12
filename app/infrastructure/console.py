import os
import re
from time import sleep

from app.domain.level import Level
from app.domain.word import Word


class Console:
    def welcome(self) -> None:
        self._clear()
        print("Bienvenidos al juego")
        print("A continuación se elegirá una palabra aleatoriamente")
        print("Debe adivinar la palabra letra por letra")
        print("Solo debe ingresar letras en minúscula")
        sleep(4)

    def interface(self, word: Word, count: int = 0) -> None:
        self._clear()
        output = ""
        for index, letter in enumerate(word.value):
            if word.mask[index]:
                output = output + letter + " "
            else:
                output = output + "_" + " "
        print(output + "     " + str(count))

    def get_level(self) -> Level:
        self._clear()
        print("Niveles:")
        print("- 1 es el nivel más fácil")
        print("- 2 es el nivel intermedio")
        print("- 3 es el nivel difícil")
        print("- 123 es el nivel DIOS")
        level = input("Ingrese el nivel que desea: ")
        return Level.from_value(level)

    @staticmethod
    def get_letter() -> str:
        while True:
            letter_in = input("Ingrese una letra: ")
            letter_in = letter_in.lower().strip()
            if bool(re.fullmatch(r"[a-zA-Z]", letter_in)):
                return letter_in

    def win(self, word: str) -> None:
        self._clear()
        print("Ganaste, la palabra era: " + word)

    def loose(self, word: str) -> None:
        self._clear()
        print("Te quedaste sin intentos, la palabra era: " + word)

    @staticmethod
    def _clear() -> None:
        os.system("clear")
