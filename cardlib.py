"""
| Computer Assignment 2

| DAT171 - Object oriented programing in Python

| Chalmers University of Technology - 2022-03-17

| by Christopher Ljungholm and David Knezevic

| This program is a library of a deck of cards for a texas holdem poker game that is going to be created on a later date.

| This assignment will focus on Object-Oriented Programming (OOP). The objective is to write a general library for standard playing cards (52 card decks). This library will be used in assignment 3 to build a simple Texas Hold’em poker game.

"""

from enum import Enum
import random
from collections import Counter
from abc import ABC
import abc


class PlayingCard(ABC):
    """Abstract class that is the base class used to create all the PlayingCard class cards needed in a deck of cards
    with all different card types, from numbered card 2 to Ace card in each suit.
    This superclass contains several subclasses.    """

    @abc.abstractmethod
    def __init__(self, suit):
        """Constructor
        :param suit: The suit of a card, ie , King card can have a suit of Spades.
        :type suit: Enum            """
        self.suit = suit

    def __eq__(self, other):
        """Defines what parameter should be base for comparing values other than equal
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool                """
        return self.get_value() == other.get_value()

    def __lt__(self, other):
        """Defines what parameter should be base for comparing values other than equal
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool                """
        return self.get_value() < other.get_value()

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str                 """
        return f"{self.get_value()} of {self.suit.name}"

    def show(self):
        """Prints self to console"""
        print(f"{self}")

    @abc.abstractmethod
    def get_value(self):
        """gets value"""
        pass

    @staticmethod
    def get_name(number):
        """This method extracts the __repr__ or __str__ from a desired value whithin the range of the
        face cards."""
        if number == 11:
            return JackCard.name
        elif number == 12:
            return QueenCard.name
        elif number == 13:
            return KingCard.name
        elif number == 14 or number == 1:
            return AceCard.name
        else:
            return number

class NumberedCard(PlayingCard):
    """The NumberedCard class is a subclass of PlayingCards which creates the cards from 2-10."""

    def __init__(self, value, suit):
        """Constructor method

        :param value: Value of card
        :type value: int
        :param suit: The suit of the playingcard.
        :type suit: Suit            """
        self.value = value
        self.suit = suit

    def get_value(self):
        """This method returns the value of the playing card
        :return self.value: The value of the object
        :rtype self.value: int      """
        return self.value

class JackCard(PlayingCard):
    """The JackCard is a subclass of PlayingCards which represents the Jack card."""
    name = 'Jack'
    def __init__(self, suit):
        """Constructor method
        :param suit: The suit of the playingcard.
        :type suit: Suit            """
        self.suit = suit

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str                 """
        return f"{self.name} of {self.suit.name}"

    def get_value(self):
        """This method returns the value of the playing card
        :return self.value: The value of the object
        :rtype self.value: int      """
        return 11

class QueenCard(PlayingCard):
    """The QueenCard is a subclass of PlayingCards which represents the Queen card."""
    name = 'Queen'
    def __init__(self, suit):
        """Constructor method
        :param suit: The suit of the playingcard.
        :type suit: Suit            """
        self.suit = suit

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str     """
        return f"{self.name} of {self.suit.name}"

    def get_value(self):
        """This method returns the value of the playing card
        :return self.value: The value of the object
        :rtype self.value: int      """
        return 12

class KingCard(PlayingCard):
    """The KingCard is a subclass of PlayingCards which represents the King card."""
    name = 'King'
    def __init__(self, suit):
        """Constructor method
        :param suit: The suit of the playingcard.
        :type suit: Suit            """
        self.suit = suit

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str     """
        return f"{self.name} of {self.suit.name}"

    def get_value(self):
        """This method returns the value of the playing card
        :return self.value: The value of the object
        :rtype self.value: int      """
        return 13

class AceCard(PlayingCard):
    """The AceCard is a subclass of PlayingCards which represents the Ace card. This library uses Ace high which means
    the value of the Ace cars is 14. The highest value card in the deck."""
    name = 'Ace'
    def __init__(self, suit):
        """Constructor method
        :param suit: The suit of the playingcard.
        :type suit: Suit            """
        self.suit = suit

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str                 """
        return f"{self.name} of {self.suit.name}"

    def get_value(self):
        """This method returns the value of the playing card
        :return self.value: The value of the object
        :rtype self.value: int      """
        return 14

class Suit(Enum):
    """The Suit class is an enumerated class that contains the four different card suits used in a classic
    deck of cards. It also assigns a value for each class for ease of sorting later on.
    """
    Hearts = 1
    Spades = 2
    Clubs = 3
    Diamonds = 4

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str                 """
        return f'{self.name}'

class StandardDeck:
    """This class represents a deck of standard playing cards containing 52 cards,
    13 of each suit and Ace as value 14."""
    def __init__(self):
        """Constructor method"""
        self.cards = []
        self.build()

    def build(self):
        """This method loops over the values and suits to create all combinations of cards, going from numbered cards to
        ace card of each suit and is called when the class is called."""
        for s in Suit:
            for v in range(2, 11):
                self.cards.append(NumberedCard(value=v, suit=s))
            self.cards.append(JackCard(s))
            self.cards.append(QueenCard(s))
            self.cards.append(KingCard(s))
            self.cards.append(AceCard(s))

    def show(self):
        """This method prints, all the cards created for and located in the deck of cards, to console."""
        for c in self.cards:
            c.show()

    def shuffle(self):
        """This method shuffles the order of cards."""
        random.shuffle(self.cards)

    def draw(self):
        """This method is for drawing a card from the created deck, it takes the top card and removes it from the deck.
        The top card being the last instance of the list cards.
        :return self.cards.pop(): Method returns removed card to variable.
        :rtype: Method          """
        return self.cards.pop()

class Hand:
    """This class represents the hand of a player, containing the cards assigned to the player."""

    def __init__(self):
        """Constructor method"""
        self.cards = []

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str                 """
        return f"Hand()"

    def __str__(self):
        """Returns a descriptive string to the object handle.
        :return: Text string
        :rtype: str                 """
        return f"The players hand, holding cards:"

    def add_card(self, addition):
        """This method adds a specific card to the empty list which is the players hand.

        :param lib: PlayingCard class with correct inputs corresponding for each subclass of PlayingCard
        :type lib: PlayingCard
        """
        self.cards.append(addition)

    def show_cards(self):
        """This method prints the players hand to console.

        :return: all cards contained in cards list prints to console
        :rtype: str
        """
        return PlayingCard.show(self.cards)

    def drop_cards(self, drop):
        """This method discards the desired card from the hand by removing it from the list cards.

        :param drop: list of cards that the user wants to drop
        :type drop: list
        """
        if isinstance(drop, int):
            drop = [drop]
        drop.sort(reverse=True)
        for i in drop:
            self.cards.pop(i)

    def sort_cards(self):
        """This method sorts the hand in regard to the value of each card"""
        sorted(self.cards, key=lambda x: x.get_value())

    def best_poker_hand(self, river=None):
        """This method calls the PokerHand class together with an input list, the river, to create
        a base for evaluation between the hand. This method is what is used to determine winning hands
        in a game of Texas Hold'em poker.

        :param river: List of PlayingCard objects that is desired to check best value with.
        :type river: list
        :return: PlayerHand object that contains the combined list from the input values.
        :rtype: PlayerHand
        """
        combined_cards = self.cards + river
        return PokerHand(combined_cards)

class PokerHand:
    """PokerHand class creates a poker hand representing the hand of the player with an addition of
    the hands value and a text string declaring what combination of cards was achieved, if any.

    """

    def __init__(self, river=[]):
        """Constructor method that sets the starting point of the PokerHands internal values.

        :param river: List of cards that will build the base for combinations and value.
        :type river: list
        """
        self.cards = []
        self.text_string = ''
        self.hand_value = Hand_Value.Highest_Card
        self.counter = PokerHand.numbifyer(river)
        self.flush = self.is_flush(river)
        self.straight = self.is_straight(river)
        self.evaluator = self.poker_hand_evaluator(river)

    def __eq__(self, other):
        """Defines what parameter should be base for comparing equal values
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool    """
        return self.evaluator == other.evaluato

    def __lt__(self, other):
        """Defines what parameter should be base for comparing values other than equal
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool    """
        return self.evaluator < other.evaluator

    def __repr__(self):
        """Determines the text string that will be showed when function is called
        :return: Text string with input argument
        :rtype: str     """
        return f"hand.PokerHand(river)"

    def __str__(self):
        """Determines the text string that will be showed when function is called
        :return: Text string with value
        :rtype: str     """
        return f"{self.text_string}"

    def poker_hand_evaluator(self, river=[]):
        """This method calculates the highest value combination of the players hand, with an option to add in the
        river, or any other list of cards of desire.

        The best hand will be determined by the loop in the method. The hand value is assigned by conditions for the
        different poker style hands. If no poker hand is achived the hand is automaticly judged by the highest card of the hand. This is done by
        adding the value for the highest hand as decimal points, after the whole number that is defined by the poker hand.

        i.e:
        A pair has value 2. If the hand consists of three cards, a pair of 4 and another card, king (value 13). The
        highest value is a king and the value of the hand will be:
        self.hand_value = 2.130404
        Where 13 stands for the king and the two 4 stands for each of the cards in the pair.

        :param river: List of PlayingCard objects that is desired to check best value with.
        :type river: list
        :return self.evaluator: Points for the hand, poker hand and highest card all in one.
        :rtype: float

        :Example:

        hand1 = Hand()
        hand1.add_cards(NumberedCard(2, Suit.Diamonds), QueenCard(Suit.Hearts))
        river = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds), NumberedCard(8, Suit.Clubs), NumberedCard(6, Suit.Spades)]
        hand_poker_values = hand1.best_poker_hand(river)

        .. seealso:: cardlib.Hand()

        """

        #     ROYAL STRAIGHT FLUSH & STRAIGHT FLUSH
        if self.flush[1] and self.straight[1] == True:
            self.add_selection(self.flush[0], self.straight[0])
            if self.straight[2] == 14 and self.straight[3] != 2:
                self.hand_value = Hand_Value.Royal_Straight_Flush
                self.text_string = f'Royal Straight Flush in {self.flush[0][1].suit.name}'
            else:
                self.hand_value = Hand_Value.Straight_Flush
                self.text_string = f'Straight Flush in {self.flush[0][1].suit.name} from {self.straight[3]} to {self.straight[2]}.'

        #           FOUR OF A KIND
        elif self.counter[0][1] == 4:
            self.hand_value = Hand_Value.Four_of_a_kind
            self.text_string = f'Four of a kind in {PlayingCard.get_name(self.counter[0][0])}.'
            self.add_selection(river, [self.counter[0][0]])

        #           FULL HOUSE
        elif self.counter[0][1] >= 3 and self.counter[1][1] >= 2:
            self.add_selection(river, [self.counter[0][0], self.counter[1][0]])
            self.hand_value = Hand_Value.Full_House
            if self.counter[1][1] == 3 and self.counter[1][0] > self.counter[0][0]:
                self.text_string = f'Full House with three {PlayingCard.get_name(self.counter[1][0])} and a pair of {PlayingCard.get_name(self.counter[0][0])}.'
            else:
                self.text_string = f'Full House with three {PlayingCard.get_name(self.counter[0][0])} and a pair of {PlayingCard.get_name(self.counter[1][0])}.'

        #             FLUSH
        elif self.flush[1] == True:
            self.add_selection(river, self.flush[0])
            self.highest_card = max(self.flush[0])
            self.hand_value = Hand_Value.Flush
            self.text_string = f'Flush in {self.cards[0].suit.name}.'


        #             STRAIGHT
        elif self.straight[1] == True:
            self.hand_value = Hand_Value.Straight
            self.text_string = f'Straight from {PlayingCard.get_name(self.straight[3])} to {PlayingCard.get_name(self.straight[2])}.'
            self.highest_card = max(self.straight[0])
            self.add_selection(river, self.straight[0])

        #           THREE OF A KIND
        elif self.counter[0][1] == 3:
            self.hand_value = Hand_Value.Three_of_a_kind
            self.text_string = f'Three of a Kind in {PlayingCard.get_name(self.counter[0][0])}.'
            self.add_selection(river, [self.counter[0][0]])

        #             TWO PAIR
        elif self.counter[0][1] == 2 and self.counter[1][1] == 2:
            self.hand_value = Hand_Value.Two_Pair
            self.text_string = f'Two Pair with {PlayingCard.get_name(self.counter[0][0])} and {PlayingCard.get_name(self.counter[1][0])}.'
            self.add_selection(river, [self.counter[0][0], self.counter[1][0]])

        #               PAIR
        elif self.counter[0][1] == 2:
            self.hand_value = Hand_Value.Pair
            self.text_string = f'Pair of {PlayingCard.get_name(self.counter[0][0])}.'
            self.add_selection(river, [self.counter[0][0]])

        #           Highest Card
        else:
            self.cards = river
            self.cards.sort(reverse=True)
            while len(self.cards) > 5:
                self.cards.pop()
            self.hand_value = Hand_Value.Highest_Card
            self.text_string = f'Highest Card {self.cards[0]}, then {self.cards[1]} followed by {self.cards[2]}.'
        self.evaluator = self.hand_value.value + PokerHand.highest_card_converter(self.cards, len(self.cards))
        return self.evaluator

    def add_selection(self, river: list, desired_values: list):
        """This method adds specific cards to the empty list which is the players poker hand if the cards exist in the
        list of card_values specified.

        :param card_list: The combined river and hand list of cards.
        :type card_list: list
        :param desired_values: A list of desired values that is to be appended to the poker hand.
        :type desired_values: list
        """
        desired_values.sort(reverse=True)
        for c in river:
            if type(desired_values[0]) == int:
                if 1 in desired_values:
                    desired_values.sort()
                    desired_values[0] = 14
                    desired_values.sort(reverse=True)
                if c.get_value() in desired_values:
                    self.cards.append(c)
            else:
                if c in desired_values:
                    self.cards.append(c)

    @staticmethod
    def numbifyer(river):
        values = []
        for c in river:
            values.append(c.get_value())
        counter = Counter(values).most_common()
        return counter

    @staticmethod
    def highest_card_converter(card_lsit, numb, exclude=[]):
        """This function takes the hand and converts the values of the cards in to a float
        that can be used to determine the total value of the highest card in decending order.

        :param card_list:
        :type card_list:
        :param numb:
        :type numb:
        :param exclude:
        :type exclude:
        """
        highest_cards = card_lsit.sort(reverse=True)
        for e in exclude:
            for i in highest_cards:
                if i.get_value() == e:
                    i.drop_cards(i)
        str_high_cards = []
        for i in range(0, numb):
            if card_lsit[i].get_value() < 10:
                str_high_cards.append((f'{card_lsit[i].get_value():02}'))
            else:
                str_high_cards.append((f'{card_lsit[i].get_value()}'))
        card_str = ''.join([str(n) for n in str_high_cards])
        add_zero = '0.'
        max_cards = float(add_zero + card_str)
        return max_cards

    @staticmethod
    def is_flush(card_list: list[PlayingCard] = []):
        """This method checks if the cards list are flush

        :return: List with first instance as a list with the flush cards and the second instance as bool True or False
        :rtype: list
        """
        flush_cards, suit_h, suit_s, suit_c, suit_d = [], [], [], [], []
        for c in card_list:
            if c.suit == Suit.Hearts:
                suit_h.append(c)
            elif c.suit == Suit.Clubs:
                suit_c.append(c)
            elif c.suit == Suit.Diamonds:
                suit_d.append(c)
            elif c.suit == Suit.Spades:
                suit_s.append(c)
            else:
                continue
        for f_list in [suit_h, suit_s, suit_c, suit_d]:
            if len(f_list) >= 5:
                for f in f_list:
                    flush_cards.append(f)
                flush_cards.sort(reverse=True)
                while len(flush_cards) > 5:
                    flush_cards.pop()
                return [flush_cards, True, flush_cards[0].suit]
            else:
                continue
        else:
            return [[], False]

    @staticmethod
    def is_straight(card_list: list[PlayingCard] = []):
        """This method checks if the cards list is straight

        :return: True or False
        :rtype: bool
        """
        numbifyed = PokerHand.numbifyer(card_list)
        values = sorted(set([i for i, j in numbifyed]), reverse=True)
        if 14 in values:
            values.append(1)
        list_organizer = []
        for i in values:
            for j in values:
                lista = list(range(i, j + 1))
                if all(k in values for k in lista):
                    if len(lista) == 5:
                        list_organizer.append(lista)
                    else:
                        continue
        if len(list_organizer) > 0:
            straight = max(list_organizer)
            if len(straight) > 0:
                return [straight, True, max(straight), min(straight)]
        else:
            return [[], False, 0, 0]

class Hand_Value(Enum):
    """Enumerated list with the values of the different hand types."""
    Highest_Card = 0
    Pair = 2
    Two_Pair = 3
    Three_of_a_kind = 4
    Straight = 5
    Flush = 6
    Full_House = 7
    Four_of_a_kind = 8
    Straight_Flush = 9
    Royal_Straight_Flush = 10

    def __repr__(self):
        """Defines the custom desired output when calling function
        :return: Name of the poker hand
        :rtype: str     """
        return f'{self.name}'

    def __eq__(self, other):
        """Defines what parameter should be base for comparing equal values
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool    """
        return self.value == other.value

    def __lt__(self, other):
        """Defines what parameter should be base for comparing values other than equal
        to same type objects.

        :param other: The value of a card, ie, King card has a value of 13
        :type other: str
        :return: True / False
        :rtype: bool    """
        return self.value < other.value