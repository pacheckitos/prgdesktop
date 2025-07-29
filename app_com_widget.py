from textual.app import App
from textual.widgets import Static

class WidgetApp(App):
    def compose(self):
        yield Static("Olá, este é um widget Static!")

if __name__ == "___main__":
    WidgetApp().run()