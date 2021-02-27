class Card:
    def __init__(self, suit: str, value: str):
        self._suit = suit
        self._value = value

    def __str__(self):
        return f"value {self._value} with suit {self._suit}"

    def __repr__(self):
        return f"value: {self._value}, suit {self._suit} \n"

    def print_card(self):
        print(f"this card is {self.value} with suit {self.suit}")
