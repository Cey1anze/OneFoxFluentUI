# coding:utf-8
from app.common.setting import ANTSWORD_PATH, TIANXIE_PATH, ALIEN_PATH, SNOWSHADOW_PATH, \
    WEBFINDER_PATH
from app.common.style_sheet import StyleSheet
from app.components.card.one_fox_v8.cards import informationCollectionCard
from app.util.utils import run_command
from app.view.baseInterface.baseInterface import BaseInterface


class InformationCollectionInterface(BaseInterface):
    """ Player interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent, objectName='InformationCollectionInterface', layoutType='normal',
                         layoutFunction=self.__initLayout)
        StyleSheet.INFORMATION_COLLECTION_INTERFACE.apply(self)
        self.register()

    def __initLayout(self):
        informationCollectionView = informationCollectionCard(self)

        self.layout.setSpacing(28)
        self.layout.setContentsMargins(40, 10, 40, 0)

        self.layout.addWidget(informationCollectionView)

    def register(self):
        # 注册每个卡片的点击处理函数
        self.registerCardClickHandler(5, self.runSnowShadow)
        self.registerCardClickHandler(6, self.runWebFinder)
        self.registerCardClickHandler(7, self.runAntSword)
        self.registerCardClickHandler(8, self.runTianXie)
        self.registerCardClickHandler(9, self.runAlien)

    def runSnowShadow(self):
        run_command(SNOWSHADOW_PATH)

    def runWebFinder(self):
        run_command(WEBFINDER_PATH, 'java', 8)

    def runAntSword(self):
        run_command(ANTSWORD_PATH)

    def runTianXie(self):
        run_command(TIANXIE_PATH, 'java', 8)

    def runAlien(self):
        run_command(ALIEN_PATH)
