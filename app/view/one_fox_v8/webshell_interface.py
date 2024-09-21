# coding:utf-8
from app.common.style_sheet import StyleSheet
from app.components.card.one_fox_v8.webshell.webshell_card import webshellCard
from app.view.baseInterface.baseInterface import BaseInterface


class WebshellInterface(BaseInterface):
    """ Player interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent, objectName='WebshellInterface', layoutType='normal', layoutFunction=self.__initLayout)
        StyleSheet.WEBSHELL_INTERFACE.apply(self)
        self.register()

    def __initLayout(self):
        webshellView = webshellCard(self)

        self.layout.setSpacing(28)
        self.layout.setContentsMargins(40, 10, 40, 0)

        self.layout.addWidget(webshellView)

    def register(self):
        # 注册每个卡片的点击处理函数
        self.registerCardClickHandler(0, self.handleButtonCardClick)
        self.registerCardClickHandler(1, self.handleAnotherCardClick)

    def handleButtonCardClick(self):
        print("Button card clicked, executing specific function for index 0")

    def handleAnotherCardClick(self):
        print("Another card clicked, executing specific function for index 1")
