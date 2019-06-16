from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import string
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1

		self.inside = GridLayout()
		self.inside.cols = 2

		self.inside.add_widget(Label(text="Zadej váhu: "))
		self.name = TextInput(multiline=False)
		print(type(self.name))
		self.inside.add_widget(self.name)

		self.add_widget(self.inside)

		self.submit = Button(text="Submit", font_size=40)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)

	def pressed(self, instance):
		name = self.name.text

		print("Váha: ", name, "kg")
		self.name.text = " "
		
		result = ((int(name) / 15) * 0.5) / 16 * 10
		result = round(result, 1)
		print(f'Kazdou hodinu vypij: {result} dcl')
		mypopup = SimplePopup()
		mypopup.open()

class Widgets(Widget):
	def btn(self):
		fire_popup()

class P(Popup):
	pass
		
class MyApp(App):
	def build(self):
		return MyGrid()


# notifikace
class SimplePopup(Popup):
   pass

class SimpleButton(Button):
   def fire_popup(self):
       pops=SimplePopup()
       show = P()
       pops = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))
       pops.open()

class SampleApp(App):
   def build(self):
       return SimpleButton()

if __name__ == '__main__':
    MyApp().run()


