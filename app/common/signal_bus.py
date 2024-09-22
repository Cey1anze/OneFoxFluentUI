# coding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal


class GlobalSignalBus(QObject):
    """ Global signal bus for shared signals """

    checkUpdateSig = pyqtSignal()
    micaEnableChanged = pyqtSignal(bool)


globalSignalBus = GlobalSignalBus()  # 全局信号总线实例


class LocalSignalBus(QObject):
    """ Local signal bus for interface-specific signals """

    sampleCardClicked = pyqtSignal(int)

