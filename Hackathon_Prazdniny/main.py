from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import string
from kivy.uix.popup import Popup
from kivy.lang import Builder


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
		notification = SimpleButton()


class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
    MyApp().run()


# notifikace
class SimplePopup(Popup):
   pass

class SimpleButton(Button):
   text = MyGrid()
   text.pressed(notification)
   def fire_popup(self):
       pops=SimplePopup()
       pops.open()

class SampleApp(App):
   def build(self):
       return SimpleButton()

SampleApp().run()