# Exam 23.7

import random
from abc import ABC, abstractmethod
from Card import Card, CardSuit, CardRank


class IDeck(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add_card(self, card: Card):
        pass


class Deck(IDeck):
    def __init__(self, shuffle=True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return self._cards.copy()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop() if self._cards else None # take the top card in the deck

    def add_card(self, card: Card):
        # self._cards.append(card)
        if card in self._cards:
            raise DeckCheatingError("Cant add a card that is already in the deck.")
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)

    def max(self):
        return max(self._cards)

    def min(self):
        return min(self._cards)


class DeckCheatingError(Exception):
    """The card already in deck."""
    pass


if __name__ == "__main__":

    deck = Deck()
    # print(f"The Number of cards in deck: {len(deck)}")

    print("Accessing cards directly by index:")
    for i in range(5):
        print(f"Card at index {i}: {deck[i]}")

    print("Iterating through all cards in the deck:")
    for card in deck:
        print(card)


    # card_drawn = deck.draw()
    # print(f"Drew card: {card_drawn}")
    #
    # print(f"Highest card: {deck.max()}")
    # print(f"Lowest card: {deck.min()}")
