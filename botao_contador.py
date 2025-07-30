from textual.app import App
from textual.widgets import Button, Static

class Contador:
    def __init__(self):
        self.valor = 0

class MVCApp(App):
    def __init__(self):
        super().__init__()
        self.contador = Contador()

    def compose(self):
        yield Button(f"Número de cliques: {self.contador.valor}", id = "btn_cnt")
        yield Static("Clique para incrementar", id = "lbl_valor")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_cnt":
            self.contador.valor += 1
            label = self.query_one("#btn_cnt", Button)
            label.label = f"Número de cliques: {self.contador.valor}"

if __name__ == "__main__":
    app = MVCApp()
    app.run()