from enum import Enum


class Level(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    GOD = 123

    @classmethod
    def from_value(cls, value: str):
        match value:
            case "1":
                return cls.LEVEL_1
            case "2":
                return cls.LEVEL_2
            case "3":
                return cls.LEVEL_3
            case "123":
                return cls.GOD
            case _:
                raise ValueError("Nivel Invalido")
