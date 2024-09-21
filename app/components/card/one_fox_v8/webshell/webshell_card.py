from app.components.sample_card import SampleCardView


def webshellCard(self):
    """ load samples """
    webshellView = SampleCardView(
        self.tr("Basic input samples"), self.scrollWidget)

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title="Button",
        content=self.tr(
            "A control that responds to user input and emit clicked signal."),
        index=0
    )

    webshellView.addSampleCard(
        icon=":/gallery/images/controls/Button.png",
        title="Button",
        content=self.tr(
            "A control that responds to user input and emit clicked signal."),
        index=1
    )

    return webshellView
