from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty,BooleanProperty
from kivymd.uix.label import MDIcon
from kivy.metrics import dp
kv = '''
<Tela>:
    MDBoxLayout:
        orientation:'vertical'
        MDRaisedButton:
            text:'data'
            on_release:table.set_data()
        SWTable:
            id:table
            size_hint:None,None
            size:dp(400),dp(200)
            sizes:[[dp(80),dp(30)],[dp(80),dp(30)],[dp(80),dp(30)],[dp(200),dp(30)],[dp(80),dp(30)]]
            header:[False,'teste','lola','teste','lola','teste']

<SWTable>:
    md_bg_color:0,0,1,1
    ScrollView:
        effect_cls:'ScrollEffect'
        MDBoxLayout:
            adaptive_width:True
            orientation:'vertical'
            MDBoxLayout:
                adaptive_height:True
                MDBoxLayout:
                    id:header
                    adaptive_size:True
            RecycleView:
                id:table
                viewclass:'SWRowTable'
                effect_cls:'ScrollEffect'
                size_hint_x: None
                RecycleBoxLayout:
                    id:table_config
                    default_size: table.width, dp(30)
                    default_size_hint: None, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
'''
class SWRowTable(MDBoxLayout):
    check = BooleanProperty(None)
    columns = ListProperty([])
    sizes = ListProperty([])
    def on_columns(self,obj,data):
        self.clear_widgets()
        self.md_bg_color = [1,0,0,1]
        self.spacing = dp(1)
        for index,text in enumerate(self.columns):
            if self.check != None and index == 0:
                self.add_widget(MDIcon(
                    icon='checkbox-intermediate' if self.check else 'checkbox-blank-outline',
                    md_bg_color=[1,1,1,1],
                    size_hint_x=None,
                    width=dp(30),
                    pos_hint={'center_y':0.5,'center_x':0.5}))
            self.add_widget(MDLabel(
                text=text,
                size_hint=[None,None],
                size=self.sizes[index],
                halign='center',
                pos_hint={'center_y':0.5,'center_x':0.5},
                md_bg_color=[1,1,1,1]
                ))

class SWTable(MDBoxLayout):
    header = ListProperty([])
    data = ListProperty([])
    sizes = ListProperty([])
    def on_data(self,obj,data):
        self.ids.table.data = data

    def on_header(self,onj,header):
        self.ids.header.clear_widgets()
        
        head = SWRowTable()
        head.sizes = self.sizes
        head.size_hint_y = None
        head.height = self.sizes[0][1]
        if header[0] in (True, False):
            self.ids.table.width = sum(x for x,y in self.sizes)+dp(30)
            head.check = False
            head.columns = header[1:]
        else:
            self.ids.table.width = sum(x for x,y in self.sizes)
            head.columns = header
            
        self.ids.header.add_widget(head)


    def set_data(self):
        self.data = [
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
            {'check':True,'sizes':self.sizes,'columns':['ola','teste','zoa','sado','aola']},
        ]
        
class Tela(MDScreen):
    ...



class Main(MDApp):
    def build(self):
        Builder.load_string(kv)
        self.tela = Tela()
        return self.tela
        
Main().run()