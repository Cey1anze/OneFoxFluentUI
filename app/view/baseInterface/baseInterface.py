from PyQt5.QtCore import Qt, QEasingCurve
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import (ScrollArea, InfoBar, ExpandLayout, FlowLayout)

from app.common.config import cfg
from app.common.signal_bus import LocalSignalBus


def defaultHandler():
    print("No specific function for this card")


class BaseInterface(ScrollArea):
    """ Base Interface with customizable layout """

    def __init__(self, parent=None, objectName='', layoutType=None, layoutFunction=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName('scrollWidget')
        self.cardClickHandlers = {}
        self._signals_connected = False

        self.localSignalBus = LocalSignalBus()

        if layoutType == 'expand':
            self.layout = ExpandLayout(self.scrollWidget)
        if layoutType == 'normal':
            self.layout = QVBoxLayout(self.scrollWidget)
            self.layout.setAlignment(Qt.AlignTop)
        elif layoutType == 'flow':
            self.layout = FlowLayout(self.scrollWidget, needAni=True)
            self.layout.setAnimation(250, QEasingCurve.OutQuad)
            self.layout.setContentsMargins(30, 0, 30, 0)
            self.layout.setVerticalSpacing(20)
            self.layout.setHorizontalSpacing(10)
        else:
            raise ValueError(f"Unknown layoutType: {layoutType}")

        self.setObjectName(objectName)
        self.__initWidget(layoutFunction)

        if not self._signals_connected:
            self.__connectSignalToSlot()
            self._signals_connected = True

    def __initWidget(self, layoutFunction):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 40, 0, 40)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        if layoutFunction:
            layoutFunction()

    def __showRestartTooltip(self):
        InfoBar.warning(
            '',
            self.tr('Configuration takes effect after restart'),
            parent=self.window()
        )

    def __connectSignalToSlot(self):
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        self.localSignalBus.sampleCardClicked.connect(self.handleCardClick)

    def handleCardClick(self, index):
        handler = self.cardClickHandlers.get(index, defaultHandler)
        # print(index)
        handler()

    def registerCardClickHandler(self, index, handler):
        """ Register A Click Handler For Each Card """
        self.cardClickHandlers[index] = handler
