from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
from Model import *


class TableScene(QGraphicsScene):
    """ A scene with a table cloth background """
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(QBrush(self.tile))


class CardItem(QGraphicsSvgItem):
    """ A simple overloaded QGraphicsSvgItem that also stores the card position """
    def __init__(self, renderer, position):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = position
        self.setScale(0.9)


def read_cards():
    """
    Reads all the 52 cards from files.
    :return: Dictionary of SVG renderers
    """
    all_cards = dict()  # Dictionaries let us have convenient mappings between cards and their images
    for suit_file, suit in zip('HSCD', range(1, 5)):  # Check the order of the suits here!!!
        for value_file, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], range(2, 15)):
            file = value_file + suit_file
            key = (value, suit)  # I'm choosing this tuple to be the key for this dictionary
            all_cards[key] = QSvgRenderer('cards/' + file + '.svg')
    return all_cards


class CardView(QGraphicsView):
    """ A View widget that represents the table area displaying a players cards. """

    # We read all the card graphics as static class variables
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = read_cards()

    def __init__(self, card_model: CardModel, card_spacing: int = 250, padding: int = 10):
        """
        Initializes the view to display the content of the given model
        :param cards_model: A model that represents a set of cards. Needs to support the CardModel interface.
        :param card_spacing: Spacing between the visualized cards.
        :param padding: Padding of table area around the visualized cards.
        """
        self.scene = TableScene()
        super().__init__(self.scene)
        self.card_spacing = card_spacing
        self.padding = padding
        self.model = card_model
        card_model.new_cards.connect(self.change_cards)
        self.change_cards()

    def change_cards(self):
        # Add the cards from scratch
        self.scene.clear()
        for i, card in enumerate(self.model):
            # The ID of the card in the dictionary of images is a tuple with (value, suit), both integers
            graphics_key = (card.get_value(), card.suit.value)
            renderer = self.back_card if self.model.flipped() else self.all_cards[graphics_key]
            c = CardItem(renderer, i)

            # Shadow effects are cool!
            shadow = QGraphicsDropShadowEffect(c)
            shadow.setBlurRadius(10.)
            shadow.setOffset(5, 5)
            shadow.setColor(QColor(0, 0, 0, 180))  # Semi-transparent black!
            c.setGraphicsEffect(shadow)

            # Place the cards on the default positions
            c.setPos(c.position * self.card_spacing, 0)
            # We could also do cool things like marking card by making them transparent if we wanted to!
            # c.setOpacity(0.5 if self.model.marked(i) else 1.0)
            self.scene.addItem(c)

        self.update_view()


    def update_view(self):
        scale = (self.viewport().height()-2*self.padding)/313
        self.resetTransform()
        self.scale(scale, scale)

        # Put the scene bounding box
        self.setSceneRect(-self.padding//scale, -self.padding//scale,
                          self.viewport().width()//scale, self.viewport().height()//scale)

    def resizeEvent(self, painter):
        # This method is called when the window is resized.
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)


class ButtonView(QWidget):
    def __init__(self, model):
        super().__init__()
        #Creating button widgets
        self.call_bet = QPushButton('Call')
        self.raise_button = QPushButton('Raise')
        self.fold_bet = QPushButton('Fold')

        #Creating raise slider and setting for it
        self.raise_slider = QSlider(Qt.Horizontal, self)
        self.raise_slider.setRange(0,100)
        self.raise_slider.setFocusPolicy(Qt.NoFocus)
        self.raise_slider.setTickInterval(20)
        self.raise_slider.setPageStep(5)
        self.raise_slider.setTickPosition(QSlider.TicksBelow)
        self.raise_slider.valueChanged.connect(self.update_raise_label)
        self.pot_label = QLabel()
        self.raise_slider.value()
        #Create raise label to track raise amount
        self.raiseLabel = QLabel('0', self)
        self.raiseLabel.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.raiseLabel.setMinimumWidth(80)

        #Betting box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.call_bet)
        vbox.addWidget(self.raise_button)
        vbox.addWidget(self.raise_slider)
        vbox.addSpacing(15)
        vbox.addWidget(self.raiseLabel)
        vbox.addWidget(self.fold_bet)
        vbox.addWidget(self.pot_label)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)

        #Betting Logic connections
        self.model = model
        model.new_pot.connect(self.update_value)


        def simplebet():
            model.bet()
        self.call_bet.clicked.connect(simplebet)

        def raiseBet():
            x=self.raise_slider.value()
            model.raise_bet(x)
        self.raise_button.clicked.connect(raiseBet)


    def update_raise_label(self, value):
        self.raiseLabel.setText(str(value))

    def update_value(self):
        self.pot_label.setText("Pot size is " + str(self.model.pot_value()) + "kr")



def buildWindow(GM):
    dealer = GM.PM.dealer
    dealer_view = CardView(dealer)

    david = GM.PM.player['David']
    #chris = GM.PM.player['Chris']
    player_view = CardView(david)

    ##### Player Cards Layout
    PlayerCardsLayout = QHBoxLayout()
    PlayerCardsLayout.addWidget(player_view)

    ##### Buttons Layout
    buttons = ButtonModel()
    buttonmama = ButtonView(buttons)
    buttonsLayout = QHBoxLayout()
    buttonsLayout.addWidget(buttonmama)

    ##### Player Layout
    PlayerLayout = QHBoxLayout()
    PlayerLayout.addLayout(PlayerCardsLayout)
    PlayerLayout.addLayout(buttonsLayout)

    ##### Dealer Layout
    DealerLayout = QVBoxLayout()
    DealerLayout.addWidget(dealer_view)

    ### Main Window Layout
    MainWindowLayout = QVBoxLayout()
    MainWindowLayout.addLayout(DealerLayout)
    MainWindowLayout.addLayout(PlayerLayout)

    win = QGroupBox('GAME')
    win.setGeometry(300, 300, 1280, 720)
    win.setLayout(MainWindowLayout)
    win.show()


