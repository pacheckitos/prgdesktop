from textual.app import App
from textual.widgets import Static

class AppMinima(App):
    
    def compose(self):
        yield Static("Olá, este é um widget Static!")

if __name__ == "__main__":
    AppMinima().run()