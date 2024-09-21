# coding:utf-8
from app.common.setting import BEHINDER_PATH, GODZILLA_PATH, ANTSWORD_PATH, TIANXIE_PATH, ALIEN_PATH
from app.common.style_sheet import StyleSheet
from app.components.card.one_fox_v8.webshell.webshell_card import webshellCard
from app.util.utils import run_command
from app.view.baseInterface.baseInterface import BaseInterface


class WebshellInterface(BaseInterface):
    """ Player interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent, objectName='WebshellInterface', layoutType='normal',
                         layoutFunction=self.__initLayout)
        StyleSheet.WEBSHELL_INTERFACE.apply(self)
        self.register()

    def __initLayout(self):
        webshellView = webshellCard(self)

        self.layout.setSpacing(28)
        self.layout.setContentsMargins(40, 10, 40, 0)

        self.layout.addWidget(webshellView)

    def register(self):
        # 注册每个卡片的点击处理函数
        self.registerCardClickHandler(0, self.runBehinder)
        self.registerCardClickHandler(1, self.runGodzilla)
        self.registerCardClickHandler(2, self.runAntSword)
        self.registerCardClickHandler(3, self.runTianXie)
        self.registerCardClickHandler(4, self.runAlien)

    def runBehinder(self):
        run_command(BEHINDER_PATH, 'java', 11)

    def runGodzilla(self):
        run_command(GODZILLA_PATH, 'java', 11)

    def runAntSword(self):
        run_command(ANTSWORD_PATH)

    def runTianXie(self):
        run_command(TIANXIE_PATH, 'java', 8)

    def runAlien(self):
        run_command(ALIEN_PATH)
