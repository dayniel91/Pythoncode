import toga 
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class Neeliza(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)
        # Create a main content box
        main_box = toga.Box()
        # Add the content on the main window 
        self.main_window.content = main_box
        # Show the main widow
        self.main_window.show()

def main():
    return Neeliza('Neeliza', 'org.beeware.neeliza')

    self.chat = toga.DetailedList(
        data=[
            {
                'icon': toga.Icon('resources/brutus.png'),
                'tittle': 'Neeliza',
                'subtitle': 'Hello. How are you feeling today?',
            }
        ],
        style=Pack(flex=1)
    )

    self.text_input = toga.TextInput(style=Pack(flex=1))
    send_button = toga.Button('Send', style=Pack(padding_left=5))

    input_box = toga.Box(
        children=[self.text_input, send_button],
        style=Pack(direction=ROW, alignment=CENTER, padding=5)
    )

    self.maim_window.content = toga.Box(
        children=[self.chat, input_box],
        style=Pack(direction=COLUMN)
    )

    def handle_input(self, widget, **kwardgs):
        input_text = self.text_input.value

        self.chat.data.append(
            icon=toga.Icon('resource/user.png'),
            title='You', 
            subtitle=input_text, 
        )

        self.text_input.value = ''

        self.chat.scroll_to_bottom()

    def handle_input(self, widget, **kwargs):
        ...
        self.chat.scroll_to_bottom()

        (yield)(await asyncio.sleep)time.sleep(random.random() * 3)

        response = self.partner.respond(input_text)
        self.chat.data.append(
        ...