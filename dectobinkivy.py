import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #widgets
#        self.window.add_widget(Image(source="20210927_083524.jpg"))

        self.title1 = Label(text="decimal to binary converter".upper(), font_size=50, color="#00FCCE")
        self.window.add_widget(self.title1)
        self.result = Label(text="resuts:", font_size = 24, color="#00FFCE")
        self.window.add_widget(self.result)
        
        
        self.num = TextInput(multiline=False, padding_y=(30,20), size_hint = (1, 0.2))
        self.window.add_widget(self.num)
        
        self.button = Button(text="convert", size_hint=(1, 0.25), bold=True, background_color='#00FFCE') 
        self.button.bind(on_press=self.main)
        self.window.add_widget(self.button)
        return self.window
      
    def main(self, instance):
    	try:
    	  dec = int(self.num.text)
    	  self.result.text = f"Binary: {bin(dec)[2:]}"
    	except ValueError:
    		self.result.text = "error"

        
        
        
        
#    def callback(self, instance):
#    	self.greeting.text = "hello " + self.user.text + "!"


if __name__ == '__main__':
    MyApp().run()
#elif menu == 2:
#binary = e.get(
#self.result.text ="Decimal: {}".format(int(binary, 2)))
#	menu = int(self.num.text)
#    	if menu < 1 or menu > 2:
#    		raise ValueError
#    	if menu == 1: