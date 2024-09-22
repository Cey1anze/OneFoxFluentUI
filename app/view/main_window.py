# coding: utf-8
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication

from qfluentwidgets import NavigationItemPosition, SplitFluentWindow, SplashScreen
from qfluentwidgets import FluentIcon as FIF

from app.view.one_fox_v8.webshell_interface import WebshellInterface
from app.view.one_fox_v8.information_collection_interface import InformationCollectionInterface
from app.view.setting_interface import SettingInterface
from app.common.config import cfg
from app.common.icon import Icon
from app.common.signal_bus import globalSignalBus
from app.common import resource


class MainWindow(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

        # TODO: create sub interface
        # self.homeInterface = HomeInterface(self)
        self.settingInterface = SettingInterface(self)
        self.webshellInterface = WebshellInterface(self)
        self.informationCollectionInterface = InformationCollectionInterface(self)

        self.connectSignalToSlot()

        # add items to navigation interface
        self.initNavigation()

    def connectSignalToSlot(self):
        globalSignalBus.micaEnableChanged.connect(self.setMicaEffectEnabled)

    def initNavigation(self):
        # self.navigationInterface.setAcrylicEnabled(True)

        # TODO: add navigation items
        self.addSubInterface(self.webshellInterface, Icon.WEBSHELL, self.tr('Webshell'), NavigationItemPosition.SCROLL)
        self.addSubInterface(self.informationCollectionInterface, Icon.INFORMATION_COLLECTION, self.tr('Information Collection'), NavigationItemPosition.SCROLL)

        # add custom widget to bottom
        self.addSubInterface(
            self.settingInterface, FIF.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)

        self.splashScreen.finish()

    def initWindow(self):
        self.resize(880, 600)
        self.setMinimumWidth(880)
        self.setWindowIcon(QIcon(':/app/images/logo.png'))
        self.setWindowTitle('OneFoxFluentUI - OFF')

        self.setCustomBackgroundColor(QColor(240, 244, 249), QColor(32, 32, 32))
        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.show()
        QApplication.processEvents()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, 'splashScreen'):
            self.splashScreen.resize(self.size())
