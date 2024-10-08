from app.components.sample_card import SampleCardView


def webshellCard(self):
    """ load samples """
    webshellView = SampleCardView(
        self.tr("Webshell"), self.scrollWidget)

    webshellView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("Behinder"),
        content=self.tr(
            '"Behinder" dynamic binary encryption website management client'),
        index=0,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("Godzilla"),
        content=self.tr(
            "Godzilla"),
        index=1,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/app/images/icons/antsword.png",
        title=self.tr("AntSword"),
        content=self.tr(
            "AntSword is a cross-platform open source website management tool"),
        index=2,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("TianXie"),
        content=self.tr(
            "Rights Management Tools"),
        index=3,
        signalBus=self.localSignalBus
    )

    webshellView.addSampleCard(
        icon=":/app/images/icons/alien.ico",
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
        icon=":/app/images/icons/Button.png",
        title=self.tr("Snow Shadow"),
        content=self.tr('IP address query, port scan, C segment survival scan, background directory scan'),
        index=5,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("Web Finder - Next"),
        content=self.tr(
            "A small tool to quickly identify ports and services"),
        index=6,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/app/images/icons/yujian.ico",
        title=self.tr("Yu Jian"),
        content=self.tr(
            "Simple and practical command line website directory scanning tool"),
        index=7,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("Tide Finger"),
        content=self.tr(
            "Fingerprint recognition gadget"),
        index=8,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/app/images/icons/fofafinder.ico",
        title=self.tr("Multiple Pupils"),
        content=self.tr(
            "Asset collection tool, supporting Quake, Fofa, Hunter and other asset mapping platform API"),
        index=9,
        signalBus=self.localSignalBus
    )

    informationCollectionView.addSampleCard(
        icon=":/app/images/icons/Button.png",
        title=self.tr("ENScan"),
        content=self.tr(
            "A tool based on the information API of major enterprises"),
        index=10,
        signalBus=self.localSignalBus
    )

    return informationCollectionView
