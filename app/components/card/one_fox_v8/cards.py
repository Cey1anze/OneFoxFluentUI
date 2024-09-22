from app.components.sample_card import SampleCardView


def webshellCard(self):
    """ load samples """
    webshellView = SampleCardView(
        self.tr("Webshell"), self.scrollWidget)

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Behinder"),
        content=self.tr(
            '"Behinder" dynamic binary encryption website management client'),
        index=0,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Godzilla"),
        content=self.tr(
            "Godzilla"),
        index=1,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("AntSword"),
        content=self.tr(
            "AntSword is a cross-platform open source website management tool"),
        index=2,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("TianXie"),
        content=self.tr(
            "Rights Management Tools"),
        index=3,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Alien"),
        content=self.tr(
            "Trojan management tool"),
        index=4,
        signalBus=self.localSignalBus
    )

    return webshellView


def informationCollectionCard(self):
    """ load samples """
    informationCollectionView = SampleCardView(
        self.tr("Information Collection"), self.scrollWidget)

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Snow Shadow"),
        content=self.tr(''),
        index=5,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Web Finder - Next"),
        content=self.tr(
            ""),
        index=6,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Yu Jian"),
        content=self.tr(
            ""),
        index=7,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Tide Finger"),
        content=self.tr(
            ""),
        index=8,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Multiple Pupils"),
        content=self.tr(
            ""),
        index=9,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Tide Finger"),
        content=self.tr(
            ""),
        index=10,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Multiple Pupils"),
        content=self.tr(
            ""),
        index=11,
        signalBus=self.localSignalBus
    )

    return informationCollectionView