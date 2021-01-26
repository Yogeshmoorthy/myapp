from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import sqlite3

class MainWindow(Screen):
    site = ObjectProperty(None)

    def search_btn(self):
        SecondWindow.current = self.site.text

        get_site = self.site.text
        get_site1 = ''
        if get_site.islower()==True:
            get_site1+=get_site.upper()
        else:
            get_site1 = get_site

        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute("SELECT * FROM contacts WHERE site_name=?",(get_site1,))
        store = c.fetchone()

        try:

            SecondWindow.owner1 = store[3]
            SecondWindow.clu_engg = store[4]
            SecondWindow.lat1 = str(store[1])
            SecondWindow.long1 = str(store[2])
            SecondWindow.engg_no1 = str(store[5])
            SecondWindow.incharge1 = store[6]
            SecondWindow.incharge_no1 = str(store[7])
            SecondWindow.managername1 = store[8]
            SecondWindow.managerno1 = str(store[9])
            SecondWindow.address1 = store[10]

            sm.current = 'second'

        except TypeError:
            mypop.popwindow(self)


class SecondWindow(Screen):

    current = ''
    owner1 = ''
    clu_engg = ''
    lat1= ''
    long1 = ''
    engg_no1 = ''
    incharge1 = ''
    incharge_no1 = ''
    managername1 = ''
    managerno1 = ''
    address1 = ''

    def on_enter(self, *args):
        self.site.text = " SITE ID : "+self.current
        self.owner.text = "OWNER : "+self.owner1
        self.engg.text = " ENGG : "+self.clu_engg
        self.lat.text = " LAT :" + self.lat1
        self.long.text = 'LONG : ' + self.long1
        self.engg_no.text = 'MOBILE : ' + self.engg_no1
        self.incharge.text = 'INCHARGE : ' + self.incharge1
        self.incharge_no.text = 'MOBILE: ' + self.incharge_no1
        self.managername.text = 'MANAGER : ' + self.managername1
        self.managerno.text = 'MOBILE : ' + self.managerno1
        self.address.text = 'ADDRESS : ' + self.address1


class WindowManager(ScreenManager):
    pass

class mypop(Screen):
    def popwindow(self):
        show = mypop()
        popupWindow = Popup(title='Warning', content=show, size_hint=(None, None), size=(400, 400))
        popupWindow.open()


Builder.load_string("""

WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name : "main"
    site : site
    GridLayout:
        cols:1
        Image:
            source : 'space.jpg' 
            opacity : 2
            
        GridLayout:
            cols : 2
            spacing : 20
            padding : 50
            
            row_force_default : True
            row_default_height : 100

            Label:
                text : "SITE ID : "
                pos_hint: {'x': 0.2, 'top': 0.8}
                size_hint : 0.1,0.1
            TextInput:
                id : site
                pos_hint: {'x': 0.2, 'top': 0.8}
                size_hint : 0.1,0.1
                multiline : False

        Button:
            text:"Search"
            pos_hint:{"x":0.2, "top": 0.2}
            size_hint : 0.6,0.6
            on_release:
                root.current='second'
                root.manager.transition.direction='left'
                root.search_btn()
<mypop>:
    Label:
        text : "Please Enter the valid SITE ID"
        auto_dismiss : True
        
    
        
<SecondWindow>:
    site : site
    owner : owner
    engg : engg
    lat : lat
    long : long
    engg_no : engg_no
    incharge : incharge
    incharge_no : incharge_no
    managername : managername
    managerno : managerno
    address : address


    FloatLayout:
        Label:
            id : site
            pos_hint: {'x': 0.2, 'top': 0.9}
            size_hint : 0.1,0.1
        Label:
            id : owner
            pos_hint: {'x': 0.5, 'top': 0.9}
            size_hint : 0.1,0.1
        Label:
            id:lat
            pos_hint: {'x': 0.2, 'top': 0.8}
            size_hint : 0.1,0.1
        Label:
            id : long
            pos_hint: {'x': 0.5, 'top': 0.8}
            size_hint : 0.1,0.1
        Label:
            id : engg
            pos_hint: {'x': 0.2, 'top': 0.7}
            size_hint : 0.1,0.1
        Label:
            id : engg_no
            pos_hint: {'x': 0.5, 'top': 0.7}
            size_hint : 0.1,0.1
        Label:
            id:incharge
            pos_hint: {'x': 0.2, 'top': 0.6}
            size_hint : 0.1,0.1
        Label:
            id : incharge_no
            pos_hint: {'x': 0.5, 'top': 0.6}
            size_hint : 0.1,0.1
        Label:
            id : managername
            pos_hint: {'x': 0.2, 'top': 0.5}
            size_hint : 0.1,0.1
        Label:
            id:managerno
            pos_hint: {'x': 0.5, 'top': 0.5}
            size_hint : 0.1,0.1
        Label:
            id : address
            pos_hint: {'x': 0.4, 'top': 0.4}
            size_hint : 0.1,0.1


        Button:
            text : 'Go Back'
            pos_hint:{"x":0.2, "top": 0.2}
            size_hint : 0.6,0.1
            on_release:
                app.root.current="main"
                root.manager.transition.direction = "right"
    
    """
)




sm=WindowManager()

screens = [MainWindow(name='main'),SecondWindow(name='second')]
for screen in screens:
    sm.add_widget(screen)

class MainApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    MainApp().run()
