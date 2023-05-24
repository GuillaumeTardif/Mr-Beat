from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class PlayIndicatorImage(Image):
    pass


class PlayIndicatorWidget(BoxLayout):
    nb_steps = 0
    indicators_lights = []
    left_align = NumericProperty(dp(0))

    def set_current_step_index(self, index):
        if index > len(self.indicators_lights):
            return
        for i in range(0, len(self.indicators_lights)):
            if i == index:
                self.indicators_lights[i].source = "images/indicator_light_on.png"
            else:
                self.indicators_lights[i].source = "images/indicator_light_off.png"

    def set_nb_steps(self, nb_steps):
        if not nb_steps == self.nb_steps:
            # Reconstruire notre layout -> mettre les boutons
            self.indicators_lights = []  # Clear la list des boutons
            self.clear_widgets()  # Clear les widgets
            dummy_widget = Widget()
            dummy_widget.size_hint_x = None
            dummy_widget.width = self.left_align
            self.add_widget(dummy_widget)
            for i in range(0, nb_steps):
                indicator_image = PlayIndicatorImage()
                indicator_image.disabled = True
                indicator_image.source = "images/indicator_light_off.png"
                self.indicators_lights.append(indicator_image)
                self.add_widget(indicator_image)
            self.nb_steps = nb_steps
