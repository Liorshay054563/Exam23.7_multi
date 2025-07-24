# Exam 23.7 oop


from Card import Card, CardSuit, CardRank
from Deck import Deck, DeckCheatingError
import random

deck = Deck()  # make the cards in deck

print("All the card in deck:")
for card in deck:  # shows all the card
    print(card)

drawn_card = deck.draw()  # take card from the deck
print()
print(f"Drew card: {drawn_card}")

new_card = Card(CardSuit.CLUBS, CardRank.TEN)

# new_card = drawn_card # return the card back - adding will success with no error handling

try:
    deck.add_card(new_card)  # adding the new card
    print(f"Added card: {new_card}")
    print()
except DeckCheatingError as e:
    print(e)


print()
print("Accessing cards directly by index:")
for i in range(len(deck)):
    print(f"In index {i} - {deck[i]}") # shows the index for each card

print()
print("The update cards in deck:")
for card in deck:
    print(card) # will be only 51 cards because we pop out card before
