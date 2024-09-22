# coding:utf-8
from app.common.setting import SNOWSHADOW_PATH, \
    WEBFINDER_PATH, YUJIAN_PATH, TIDE_PATH, MULTIPLEPUPILS_PATH, GOLIN_PATH
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
        self.registerCardClickHandler(5, self.runSnowShadow)
        self.registerCardClickHandler(6, self.runWebFinder)
        self.registerCardClickHandler(7, self.runYuJian)
        self.registerCardClickHandler(8, self.runTide)
        self.registerCardClickHandler(9, self.runMultiplePupils)
        self.registerCardClickHandler(10, self.runGOlin)

    def runSnowShadow(self):
        run_command(SNOWSHADOW_PATH)

    def runWebFinder(self):
        run_command(WEBFINDER_PATH, 'java', 8)

    def runYuJian(self):
        run_command(YUJIAN_PATH)

    def runTide(self):
        run_command(TIDE_PATH)

    def runMultiplePupils(self):
        run_command(MULTIPLEPUPILS_PATH)

    def runGOlin(self):
        run_command(GOLIN_PATH, None, None, 'web')
