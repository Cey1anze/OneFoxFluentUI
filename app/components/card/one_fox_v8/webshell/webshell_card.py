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
        index=0
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Godzilla"),
        content=self.tr(
            "Godzilla"),
        index=1
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("AntSword"),
        content=self.tr(
            "AntSword is a cross-platform open source website management tool"),
        index=2
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("TianXie"),
        content=self.tr(
            "Rights Management Tools"),
        index=3
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title=self.tr("Alien"),
        content=self.tr(
            "Trojan management tool"),
        index=4
    )

    return webshellView
