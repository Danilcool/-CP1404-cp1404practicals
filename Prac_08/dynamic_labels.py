from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        # list of names
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

        # create a box layout
        main_layout = BoxLayout(orientation='vertical')

        # create a label for each name
        for name in names:
            label = Label(text=name, font_size=32)
            main_layout.add_widget(label)

        return main_layout


DynamicLabelsApp().run()