from textual.app import App, ComposeResult
from textual.widgets import Static, Label, Header, Footer, OptionList, Button
from textual.containers import Horizontal, Vertical

import src.classes as c
from src.data import *

class RPGApp(App):
    CSS_PATH = "game.tcss"

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal():

            yield OptionList("Barbarian", "Mage", "Knight", id="class_list")

            with Vertical(id="desc_container"):
                yield Static("Select a class to see details", id="class_desc")

        yield Footer()

    def on_option_list_option_highlighted(self, event: OptionList.OptionHighlighted):
                selected_class = event.option.prompt

                self.query_one("#class_desc", Static).update(classes[selected_class].description)

app = RPGApp()
app.run()