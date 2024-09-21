# coding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal


class SignalBus(QObject):
    """ Signal bus """

    sampleCardClicked = pyqtSignal(int)
    checkUpdateSig = pyqtSignal()
    micaEnableChanged = pyqtSignal(bool)


signalBus = SignalBus()
