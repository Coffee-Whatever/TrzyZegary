import kivy
# from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime
import pytz
import time

kivy.require('2.1.0')
Window.size = (900, 900)


class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.000001)

    def update(self, what='useless'):
        self.time1.text = str(datetime.now(pytz.timezone("Europe/Warsaw")))
        self.time2.text = str(datetime.now(pytz.timezone("America/New_York")))
        self.time3.text = str(datetime.now(pytz.timezone("Europe/London")))


Builder.load_string(
"""
<Screen>:
    label1:label1
    label2:label2
    label3:label3
    time1:time1
    time2:time2
    time3:time3
    GridLayout:
        cols:2
        size:root.size
        Label:
            id:label1
            text:'Polska Warszawa'
            canvas.before:
                Color:
                    rgba: 94/255,58/255,58/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            id:time1
            text:'czas 1'
            canvas.before:
                Color:
                    rgba: 137/255,35/255,35/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            id:label2
            text:'New York'
            canvas.before:
                Color:
                    rgba: 137/255,35/255,35/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            id:time2
            text:'czas 2'
            canvas.before:
                Color:
                    rgba: 94/255,58/255,58/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            id:label3
            text:'Londyn'
            canvas.before:
                Color:
                    rgba: 94/255,58/255,58/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            id:time3
            text:'czas 3'
            canvas.before:
                Color:
                    rgba: 137/255,35/255,35/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size
"""
)

class MyApp(App):
    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()
