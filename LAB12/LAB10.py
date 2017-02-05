# Jose Capestany
# CS126L
# 5/13/2016
# LAB12: BlackJack
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

class BlackjackHand():

    # Initialize the hand
    def __init__(self):
        self._hand = []
        
    # Adds a card object to the hand
    def add_card(self, new_card):
        self._hand.append(new_card)
        
    # Returns the str of each card in the hand
    def __str__(self):
        for i in self._hand:
            print(i, end = ', ')
        return ''

    # Finds the value of the hand
    def get_value(self):
        sum = 0
        for i in self._hand:
            sum += i.get_value()
        return sum

class Blackjack():

    # Initializes the deck and the bank
    def __init__(self, starting_dollars):
        self.bank = ChipBank(starting_dollars)
        self.deck = []
        self.active = False
        for i in range(52):
            self.deck.append(Card(i))

    # Draws a card and removes it from the deck
    def draw(self):
        draw = random.choice(self.deck)
        self.deck.remove(draw)
        return draw

    # Draws the dealer and player's starting hands of blackjack
    def start_hand(self, wager):
        self.active = True
        self.wager = wager
        self.bank.withdraw(wager)
        self.hand = BlackjackHand()
        self.dealer = BlackjackHand()
        self.hand.add_card(self.draw())
        facedown = self.draw()
        facedown.face_down()
        self.dealer.add_card(facedown)
        self.hand.add_card(self.draw())
        self.dealer.add_card(self.draw())
        print('Your starting hand:')
        print(self.hand)
        print("Dealer's starting hand:")
        print(self.dealer)
        if self.hand.get_value() == self.dealer.get_value() == 21:
            print('You both got blackjack!')
            self.end_hand('push')
        elif self.hand.get_value() == 21:
            print('Blackjack!')
            self.end_hand('win')
        elif self.dealer.get_value() == 21:
            print('Dealer gets blackjack!')
            self.end_hand('lose')

    # The player stops interacting and the dealer draws until value is > 16
    def stand(self):
        self.dealer._hand[0].face_up()
        print('Dealers hand:')
        print(self.dealer)
        while self.dealer.get_value() < 16:
            draw = self.draw()
            print('Dealer draws ' + str(draw))
            self.dealer.add_card(draw)
            print('Dealers hand:')
            print(self.dealer)
        if self.dealer.get_value() > 21:
            print('Dealer busts!')
            self.end_hand('win')
        elif self.dealer.get_value() > self.hand.get_value():
            self.end_hand('lose')
        elif self.dealer.get_value() == self.hand.get_value():
            self.end_hand('push')
        else:
            self.end_hand('win')

    # The player draws a card and adds it to their hand
    def hit(self):
        draw = self.draw()
        print('You draw ' + str(draw))
        self.hand.add_card(draw)
        print(self.hand)
        if self.hand.get_value() == 21:
            self.end_hand('win')
        elif self.hand.get_value() > 21:
            print('You bust!')
            self.end_hand('lose')

    # Depending on the outcome the money is distrbuted
    # Also, creates a brand new deck
    def end_hand(self, outcome):
        if outcome == 'win':
            print('You win!')
            self.bank.deposit(2 * self.wager)
        elif outcome == 'lose':
            print('You lose!')
        elif outcome == 'push':
            print('You push!')
            self.bank.deposit(self.wager)
        self.active = False
        self.deck = []
        for i in range(52):
            self.deck.append(Card(i))

    # If end_hand occured the game is over
    def game_active(self):
        if self.active:
            return True
        else:
            return False

# TEST CODE
if __name__ == '__main__':
    blackjack = Blackjack(250)
    while blackjack.bank.value > 0:
        print('Your remaining chips: ' + str(blackjack.bank))
        wager = int(input('How much would you like to wager? '))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input('STAND or HIT: ').upper()
            if choice == 'STAND': blackjack.stand()
            elif choice == 'HIT': blackjack.hit()
        print()
    print('Out of money! The casino wins!')
