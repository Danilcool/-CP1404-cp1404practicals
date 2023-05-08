from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        self.root.ids.my_label.text = "Greet"
        self.root.ids.output_label.text = "two"
        return self.root

    def input_name(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_pressed(self):
        self.root.ids.my_label.text = "HELLO"

    def clear(self):
        self.root.ids.my_label.text = "Greet"
        self.root.ids.output_label.text = "two"

BoxLayoutDemo().run()
