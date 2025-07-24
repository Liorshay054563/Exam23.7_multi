# exam 23.7

from abc import ABC, abstractmethod
from enum import Enum


class ICard(ABC):
    @abstractmethod
    def suit(self):
        pass

    @abstractmethod
    def rank(self):
        pass


class CardSuit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


class CardRank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card(ICard):
    def __init__(self, suit: CardSuit, rank: CardRank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def get_display_name(self):
        return f"{self.rank.name} : {self.suit.value}"

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False

    def __lt__(self, other):
        if self.rank.value == other.rank.value:
            return self.suit.value < other.suit.value
        return self.rank.value < other.rank.value

    def __gt__(self, other):
        if self.rank.value == other.rank.value:
            return self.suit.value > other.suit.value
        return self.rank.value > other.rank.value

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __str__(self):
        return self.get_display_name()
    def __repr__(self):
        return f"Card(suit={self.suit}, rank={self.rank})"


# card = Card("Hearts", "Ace")
# print(card)