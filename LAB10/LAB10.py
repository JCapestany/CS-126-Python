# Jose Capestany
# CS126L
# 4/22/2016
# LAB10: Casino Night
import random


class Card():

    # Initializes all the revelent variables
    def __init__(self, card_num):
        card_set = ('Ace', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'Jack', 'Queen', 'King', 11,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        if card_num < 13:
            self._suit = 'Spades'
        elif card_num < 26:
            self._suit = 'Hearts'
        elif card_num < 39:
            self._suit = 'Clubs'
        else:
            self._suit = 'Diamonds'
        rank_num = card_num % 13
        self._rank = card_set[rank_num]
        self._value = card_set[rank_num + 13]
        self._faceup = True
        self._card = self._rank + ' of ' + self._suit

    # Returns the actual card
    def __str__(self):
        if self._faceup is False:
            return '<facedown>'
        else:
            return self._card

    # Returns the suit
    def get_suit(self):
        return self._suit

    # Returns the rank
    def get_rank(self):
        return self._rank

    # Returns the value
    def get_value(self):
        return self._value

    # Sets the card face down
    def face_down(self):
        self._faceup = False

    # Sets the card face up
    def face_up(self):
        self._faceup = True


class ChipBank():

    # Initializes the relevant variable
    def __init__(self, value):
        self.value = value

    # Returns the value in poker chips
    def __str__(self):
        black = self.value // 100
        green = (self.value - black * 100) // 25
        red = (self.value - black * 100 - green * 25) // 5
        blue = self.value - black * 100 - green * 25 - red * 5
        return '%d blacks, %d greens, %d reds, %d blues - totaling $%d' % (
            black, green, red, blue, self.value)

    # Reduce the value and return the amount reduced
    def withdraw(self, amount):
        if amount > self.value:
            amount = self.value
        self.value -= amount
        return amount

    # Increase the value by the amount
    def deposit(self, amount):
        self.value += amount


# I changed test code to make the program pep8 compliant
# DO NOT CHANGE TEST CODE #####
if __name__ == "__main__":
    # Lets make a deck of cards
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        # print each card as we add them
        print(my_card)

    # print a random card from the deck
    print(random.choice(deck))

    # In my implementation , card number 37 is the queen of clubs
    card = Card(37)
    print(card)
    # Queen of Clubs
    print(card.get_value())
    # 10
    print(card.get_suit())
    # Clubs
    print(card.get_rank())
    # Queen
    card.face_down()
    print(card)
    # <facedown>
    card.face_up()
    print(card)
    # Queen of Clubs

    cs = ChipBank(149)
    print(cs)
    # 1 blacks, 1 greens, 4 reds, 4 blues - totaling $149
    cs.deposit(7)
    print(cs.value)
    # 156
    print(cs)
    # 1 blacks, 2 greens, 1 reds, 1 blues - totaling $156
    print(cs.withdraw(84))
    # 84
    print(cs)
    # 0 blacks, 2 greens, 4 reds, 2 blues - totaling $72
    cs.deposit(120)
    print(cs)
    # 1 blacks, 3 greens, 3 reds, 2 blues - totaling $192
    print(cs.withdraw(300))
    # 192
