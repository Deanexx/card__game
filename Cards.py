from Card import Card
import random


class Cards:
    def __init__(self):
        self.suits = {"♥", "♣", "♠", "♦"}
        self.values = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        self.__deck = []

        self.__create__deck()  # once instance created calling method to fill __deck

    def __call__(self):
        return self.__deck

    def __create__deck(self):
        for i in self.suits:
            for j in self.values:
                self.__deck.append(Card(i, j))

    def print__deck(self):
        for i in self.__deck:
            print(i)
        # return self.__deck  #this line in case print with __repr__

    def shuffle__deck(self):
        random.shuffle(self.__deck)

    def remove__card(self):
        if self.__deck:
            rand_num = random.randrange(0, len(self.__deck) - 1)
            return self.__deck.pop(rand_num)
        return None

    def card__left(self):
        return len(self.__deck)
