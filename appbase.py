from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.binding import Binding

class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Esta é a tela inicial.")
        yield Footer()

class TelaSecundaria(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Esta é a tela secundária.")
        yield Footer()

class TelaAjuda(Screen):

    def compose(self):
        yield Header(icon = "?", show_clock = True,  time_format = "%H:%M")
        yield Static("Esta é a tela de ajuda!")
        yield Footer(show_command_palette = False)

    def on_mount(self):
        self.sub_title = "Ajuda"

class AppBase(App):
    TITLE = "Aplicação base"
    SUB_TITLE = "(Início)"

    SCREENS = {
        "inicial": TelaInicial,
        "secundaria": TelaSecundaria,
        "ajuda" : TelaAjuda
    }

    BINDINGS = [
        Binding("n", "ir_para_secundaria", "Ir para tela secundária"),
        Binding("b", "voltar", "Voltar para tela anterior"),
        Binding("s", "switch_inicial", "Switch para tela inicial"),
        Binding("?", "ir_para_ajuda", "Ir para a tela de ajuda")
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock = True)
        yield Static()
        yield Footer()

    def on_mount(self):
        self.push_screen("inicial")

    def action_ir_para_secundaria(self):
        self.push_screen("secundaria")

    def action_voltar(self):
        self.pop_screen()

    def action_switch_inicial(self):
        self.switch_screen("inicial")

    def action_ir_para_ajuda(self):
        self.switch_screen("ajuda")

if __name__ == "__main__":
    AppBase().run()