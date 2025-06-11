class Word:
    def __init__(self, value: str) -> None:
        self.value = value
        self.mask = [False for _ in value]

    def __len__(self) -> int:
        return len(self.value)
