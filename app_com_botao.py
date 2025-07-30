from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class BotaoApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Clique aqui", id = "meu_botao")
        yield Static("Aguardando interação...", id = "mensagem")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        mensagem = self.query_one("#mensagem", Static)
        mensagem.update("Você clicou no botão!")
        
if __name__ == "__main__":
    BotaoApp().run()