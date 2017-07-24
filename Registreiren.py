from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from passlib.hash import pbkdf2_sha256
from Hauptseite import*

#from kivy.uix.button import button
Hauptfenster = MyApp.build(App)

Builder.load_string("""

<GirisEkrani>:
    GridLayout:
        rows:9
        cols:


    #    Label:
    #        text:"Konto"
    #        text_size: self.size
    #        halign: 'right'
    #        valign: 'middle'


    #    Label:
    #        text:" erstellen"
    #        text_size: self.size
    #        halign:"left"
    #        valign:"middle"
    #        size_hint:1,4

        FloatLayout:
        Label:
            text:""
            bgcolor:None
            canvas.before:
                Color:
                    rgb :0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size



        FloatLayout:
        Label:
            text:"Registrierung"
            size_hint:2,2
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size




        Label:
            text:"Handy Nummer"
            size_hint: 0.1,0.2


        TextInput:
            id:Handy Nummer
            multiline: False



        Label:
            text: "Email Adresse"                                                    #Password ist chat(wird Verschlüsselt angezeigt)
            #font_size: "10sp"
            size_hint: 0.1,0.1

        TextInput:
            id:email
            multiline: False


        Label:
            text:"Password"
            font_size: "15sp"
            size_hint: 1,1



        TextInput:
            id:passwd
            multiline:False
            password:True


        Label:
            text:"Password wiederholen"
            front_size:"12"

        TextInput:
            text:
            id:passwd
            multiline:False
            password:True

        Label:                                                                  #Platzsparer

        Button:
            text: "login"
            pos_hint:{'left_x':.50, 'left_y':.50}
            on_press:root.Fenster



        Label:
            text:
            id:email
            multiline:False
            size_hint:1,4

        Button:
            text:"bereits Registriert"
            pos_hint:{'center_x':.50, 'right_y':.5}
            size_hint:0,0
            on_press:root.build()




<GirisOnayEkrani>:                                                              #nächste seite, nach der anmeldung





<GirisRedEkrani>:
    BoxLayout:
        orientation: "vertical"




<RootWidget>:
    id: kok
    GirisEkrani:
        id: giris
        name: "giris_ekrani"
    GirisOnayEkrani:
        id: onay
        name: "giris_basarili"
    GirisRedEkrani:
        id: red
        name: "giris_hatali"



""")



class GirisEkrani(Screen):
    def login(self):
        if self.ids.HandyNummer.text == "" and \
            self.ids.email.text ==  "" and \
            self.ids.passwd.text == "" and \
            self.ids.passwd.text == "":
            self.manager.current = "giris_basarili"
        password = open("password.txt", "w")
#class GirisEkrani(Screen):
    def Fenster():
        Hauptfenster.run()

class Registrierung(Screen):
    def login(self):
        while password1!=password2:
            password1=input("Enter your Password: ")
            password2=input("Confirm your Password: ")
            Pass_ok=True
        password = open("password.txt", "w")


    def incomingData(self, req, results):
        sicaklik = data["list"][0]["main"]["temp"]-273.15



class GirisOnayEkrani(Screen):
    pass

class GirisRedEkrani(Screen):
    def anaEkranaDon(self):
        self.manager.current = "giris_ekrani"

class RootWidget(ScreenManager):
    pass

class GirisSistemiApp(App):
    def build(self):
        return RootWidget()

class Manny(App):
    def next(self):
        return GirisSistemiApp()


class MenuScreen(Screen):
    pass
class SettingScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget()


if __name__ == "__main__":
    GirisSistemiApp().run()






    #Quellen:
            #https://www.gurayyildirim.com.tr/kivy-course-10-user-login-system-with-kivy-1203.html
            #https://kivy.org/docs/guide/widgets.html
