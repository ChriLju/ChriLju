from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from View import *
from Model import *
qt_app = QApplication(sys.argv)



GM = GameModel()
GM.start()

buildWindow(GM)


qt_app.exec_()
