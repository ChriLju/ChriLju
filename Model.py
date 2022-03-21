from PyQt5.QtCore import *
from abc import abstractmethod
from cardlib import *


class CardModel(QObject):
    """ Base class that described what is expected from the PlayerView widget """

    new_cards = pyqtSignal()  #: Signal should be emited when cards change.

    @abstractmethod
    def __iter__(self):
        """Returns an iterator of card objects"""

    @abstractmethod
    def flipped(self):
        """Returns true of cards should be drawn face down"""


class GameModel(QObject):
    data_changed = pyqtSignal()
    game_message = pyqtSignal((str,))

    def __init__(self):#, players):
        super().__init__()
        self.running = False
        self.player_turn = -1
        self.player_list = ['Chris', 'David', 'Adam']
        self.PM = PlayerManager(self.player_list)


    def start(self):
        if self.running:
            self.game_message("Can't start game. Game already running.")
        self.PM = PlayerManager(self.player_list)
        self.PM.player_startup_creation()
        self.PM.dealer.burn_card()
        self.PM.dealer.flop()
        for player in self.PM.player.values():
            player.add_card(self.PM.dealer.draw())
            player.add_card(self.PM.dealer.draw())
        self.running = True
        self.player_turn = 0


class PlayerManager:
    def __init__(self, player_list=[]):
        #self.name = PM
        self.player = {}
        self.player_list = player_list

    def player_startup_creation(self):
        self.dealer = Dealer()
        #GameModel.dealer = self.dealer
        for name in self.player_list:
            self.player[name] = Player()

    def create_new_player(self, name: str):
        number = 1
        if name in self.player_list:
            name = name+str(number)
            number += 1
        self.player_list.append(str(name))
        self.player[str(name)] = Player()

    def remove_player(self, name: str):
        del self.player[name]
        self.player_list.remove(str(name))

    def set_active(self):
        """
        Selects the active players for the round.
        :return:
        """
        for player in self.player:
            if player.active:
                active_player = player
                player.hand.flipped_cards = True
            else:
                inactive_player = player
                player.hand.flipped_cards = False
        self.data_changed.emit()
        return active_player, inactive_player


"""
class MySimpleCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

# You have made a class similar to this (hopefully):
class Hand:
    def __init__(self):
        # Lets use some hardcoded values for most of this to start with
        self.cards = [MySimpleCard(13, 2), MySimpleCard(7, 0), MySimpleCard(13, 1)]

    def add_card(self, card):
        self.cards.append(card)

"""


class Player(Hand, CardModel):
    def __init__(self):
        Hand.__init__(self)
        CardModel.__init__(self)
        #Money.__init__(self)
        # Additional state needed by the UI
        self.flipped_cards = False

    def __iter__(self):
        return iter(self.cards)

    def flip(self):
        # Flips over the cards (to hide them)
        self.flipped_cards = not self.flipped_cards
        self.new_cards.emit()  # something changed, better emit the signal!

    def flipped(self):
        # This model only flips all or no cards, so we don't care about the index.
        # Might be different for other games though!
        return self.flipped_cards

    def add_card(self, card):
        super().add_card(card)
        self.new_cards.emit()  # something changed, better emit the signal!


class Dealer(StandardDeck, CardModel):
    def __init__(self):
        CardModel.__init__(self)
        self.cards = StandardDeck().cards
        self.river = []
        self.shuffle()
        #self.add_card()
        self.burned_cards = []

    def __iter__(self):
        return iter(self.river)

    def __str__(self):
        return f'Dealer'

#    def give_card(self, name):
#        PM.player[name].cards.add_card(self.cards)

    def add_card(self):
        """This method adds a specific card to the empty list which is the cards on the table.

        :param lib: Dealer class with correct inputs corresponding for each subclass of PlayingCard
        :type lib: PlayingCard      """
        return self.river.append(self.draw())

    def burn_card(self):
        del self.cards[-1]

    def flop(self):
        self.add_card()
        self.add_card()
        self.add_card()

    def new_deck(self):
        self.cards = StandardDeck().cards

class ButtonModel(QObject):
    new_pot = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.value = 0

    def pot_value(self):
        return self.value

    def bet(self):
        self.value += 1
        self.new_pot.emit()

    def raise_bet(self, raise_amount):
        self.value +=raise_amount
        self.new_pot.emit()
    def Fold(self):
        pass

class PlayerModel(QObject):
    pass

class Money:
    def __init__(self):
        self.money = 500
        pass
    pass


class Betting:
    def __init__(self):
        self.bb = self.money / 50
        self.sb = self.bb / 2
        self.pot = 0
    pass

