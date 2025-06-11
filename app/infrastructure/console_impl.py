import os
from time import sleep
from typing import override

from app.domain.console import Console
from app.domain.level import Level
from app.domain.word import Word


class ConsoleImpl(Console):
    @override
    def welcome(self) -> None:
        self._clear()
        print("Bienvenidos al juego")
        print("A continuación se elegirá una palabra aleatoriamente")
        print("Debe adivinar la palabra letra por letra")
        print("Solo debe ingresar letras en minúscula")
        sleep(5)
        self._clear()

    @override
    def interface(self, word: Word, count: int = 0) -> None:
        self._clear()
        output = ""
        for index, letter in enumerate(word.value):
            if word.mask[index]:
                output = output + letter + " "
            else:
                output = output + "_" + " "
        print(output + "     " + str(count))

    @staticmethod
    @override
    def get_level() -> Level:
        level = input(
            "Ingrese el nivel que desea:\n- 1 es el nivel más fácil\n- 2 es el nivel intermedio\n- 3 es el nivel difícil\n- 123 es el nivel GOD\n"
        )
        return Level.from_value(level)

    @staticmethod
    @override
    def get_letter() -> str:
        letter_in = input("Ingrese una letra: ")
        if (90 < ord(letter_in) < 97) or ord(letter_in) < 65:
            raise ValueError("Por favor ingrese una letra")
        elif ord(letter_in) > 122 and ord(letter_in) != 241 and ord(letter_in) != 209:
            raise ValueError("Por favor ingrese una letra")
        elif 65 <= ord(letter_in) <= 90:
            letter_in = chr(ord(letter_in) + 32)
        elif ord(letter_in) == 209:
            letter_in = chr(241)
        return letter_in

    @staticmethod
    @override
    def win(word: str) -> None:
        print("\nGanaste, la palabra era: " + word)

    @staticmethod
    @override
    def loose(word: str) -> None:
        print("Te quedaste sin intentos, la palabra era: " + word)

    @staticmethod
    def _clear() -> None:
        os.system("clear")
