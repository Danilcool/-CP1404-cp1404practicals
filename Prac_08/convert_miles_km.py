"""
CP1404/CP5632 Practical
Miles to Kilometres Converter
Danil, IT@JCU
Started 05/08/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Danil Ovcharenko'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 600)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root



    def add_value(self,value):
        result = int(value) + 1
        self.root.ids.input_number.text = str(result)

    def reduce_value(self,value):
        result = int(value) - 1
        self.root.ids.input_number.text = str(result)

    def convert_miles_to_km(self,miles):
        conversion_factor = 0.62137119
        result = int(miles) / conversion_factor
        self.root.ids.kilometers_value.text = str(result)

SquareNumberApp().run()
