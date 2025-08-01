from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual.events import Click

class LabelPressedApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Pressione aqui!", id = 'lbl_pressione')


    def on_click(self, event: Click):
        lbl : Label = event.widget
        lbl.update("Pressionou!")


if __name__ == "__main__":
    app = LabelPressedApp()
    app.run()