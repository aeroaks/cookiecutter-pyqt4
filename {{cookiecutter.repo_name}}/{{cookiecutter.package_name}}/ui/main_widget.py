import os
import json
from collections import OrderedDict

from PyQt4 import QtGui
from PyQt4 import QtCore

from src.ep_widgets import *

class MainWidget(QtGui.QWidget):
    """Class for displaying osa registration related ui elements."""

    def __init__(self, main_, parent=None):
        super().__init__(parent)
        self.name = 'main_widget'
        self.setObjectName(self.name)

        self.main_ = main_
        logging.debug('main widget init')
        self.init_ui()

    def reset_ui(self):
        # reset ui for next test
        logging.debug('reset_ui')

    def init_ui(self):
        """setup structure/layout to the tab
        """

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)

        self.vbox = QtGui.QVBoxLayout(self)
        self.vbox.setObjectName('operator_vbox')
