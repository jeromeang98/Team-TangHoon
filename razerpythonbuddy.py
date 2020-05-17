import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, TransitionBase
from kivy.lang import Builder
 
 
class Profile(Screen):
    pass
 
class Finance(Screen):
    pass
 
class Razerpay(Screen):
    pass
 
class Expenses(Screen):
    pass
 
class Initial_page(Screen):
    pass
 
class Login(Screen):
    pass
 
class Loginwelcome(Screen):
    pass
 
class Signup(Screen):
    pass
 
class Signupwelcome(Screen):
    pass
 
class Scan(Screen):
    pass
 
class QRcode(Screen):
    pass
 
class Transfer(Screen):
    pass
 
class Pocket(Screen):
    pass
 
class Transaction(Screen):
    pass
 
class Expendituresum(Screen):
    pass
 
class Investmenttopics(Screen):
    pass
 
class Wdwpage(ScreenManager):
    pass
 
kv = Builder.load_file('razer.kv')
 
class Razerbuddy(App):
    def build(self): 
        return kv
 
if __name__ == "__main__":
    Razerbuddy().run()